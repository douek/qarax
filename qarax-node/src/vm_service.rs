use crate::vmm_handler::node::node_server::Node;
use crate::vmm_handler::node::{
    Response as NodeResponse, Status as NodeStatus, VmConfig, VmId, VmList,
};
use crate::vmm_handler::VmmHandler;

use std::collections::HashMap;
use std::sync::Arc;
use tokio::sync::RwLock;
use tonic::{Code, Request, Response, Status};

use anyhow::Result;

#[derive(Debug)]
pub struct VmService {
    // TODO: Not sure about this at all
    handlers: Arc<RwLock<HashMap<String, VmmHandler>>>,
}

impl VmService {
    pub fn new() -> Self {
        VmService {
            handlers: Arc::new(RwLock::new(HashMap::new())),
        }
    }
}

#[tonic::async_trait]
impl Node for VmService {
    async fn start_vm(&self, request: Request<VmConfig>) -> Result<Response<VmConfig>, Status> {
        let mut config = request.into_inner();
        tracing::info!(
            "Starting VM {}, {}, {}",
            &config.vm_id,
            &config.memory,
            &config.vcpus
        );

        let mut handlers = self.handlers.write().await;
        let handler = handlers
            .entry(config.vm_id.to_owned())
            .or_insert_with(VmmHandler::new);

        handler
            .configure_vm(&mut config)
            .await
            .map_err(|e| Status::internal(e.to_string()))?;

        tracing::info!("Configured VM...");
        handler
            .start_vm()
            .await
            .map_err(|e| Status::internal(e.to_string()))?;
        tracing::info!("Started VM...");

        Ok(Response::new(config))
    }

    async fn stop_vm(&self, request: Request<VmId>) -> Result<Response<NodeResponse>, Status> {
        let vm_id = request.into_inner().vm_id;
        tracing::info!("Stopping VM {}", vm_id);
        tracing::info!("handlers available");

        let mut handlers = self.handlers.write().await;

        if let Some(handler) = handlers.get(&vm_id) {
            tracing::info!("Fetched handler for vm {}", vm_id);
            handler
                .stop_vm()
                .await
                .map_err(|e| Status::internal(e.to_string()))?;

            handlers.remove(&vm_id);
            let response = NodeResponse {
                status: NodeStatus::Success as i32,
            };

            Ok(Response::new(response))
        } else {
            Err(Status::new(Code::FailedPrecondition, "vm not found"))
        }
    }

    async fn list_vms(&self, request: Request<()>) -> Result<Response<VmList>, Status> {
        tracing::debug!("Got a request: {:?}", request);

        let response = VmList {
            vm_id: vec![String::from("123")],
        };

        Ok(Response::new(response))
    }

    async fn health_check(&self, request: Request<()>) -> Result<Response<NodeResponse>, Status> {
        tracing::debug!("Got a request: {:?}", request);

        let response = NodeResponse {
            status: NodeStatus::Success as i32,
        };

        Ok(Response::new(response))
    }
}

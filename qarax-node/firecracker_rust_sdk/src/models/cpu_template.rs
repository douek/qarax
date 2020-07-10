/*
 * Firecracker API
 *
 * RESTful public-facing API. The API is accessible through HTTP calls on specific URLs carrying JSON modeled data. The transport medium is a Unix Domain Socket.
 *
 * The version of the OpenAPI document: 0.21.0
 * Contact: compute-capsule@amazon.com
 * Generated by: https://openapi-generator.tech
 */

/// CpuTemplate : The CPU Template defines a set of flags to be disabled from the microvm so that the features exposed to the guest are the same as in the selected instance type.

/// The CPU Template defines a set of flags to be disabled from the microvm so that the features exposed to the guest are the same as in the selected instance type.
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum CpuTemplate {
    #[serde(rename = "C3")]
    C3,
    #[serde(rename = "T2")]
    T2,
}

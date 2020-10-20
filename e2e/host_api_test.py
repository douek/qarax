import qarax
from qarax import Host
from qarax.rest import ApiException
import sys
import time
import logging


def poll_status(get_host):
    # need to keep polling host until status is up
    # set timer
    timer = time.time()
    timeout = 20 #secs
    host = get_host()
    while host.status != 'Up':
        # Get host by ID
        if (time.time() > timer + timeout):
            raise Exception("installing time passed")
        time.sleep(5)
        host = get_host()
    return True

def hosts_api(api_client, host_config, node_config):
    logging.basicConfig(filename='host-api.log',level=logging.INFO)
    try:
        api_instance = qarax.HostsApi(api_client)
        host = Host(
            name='hostoTest',
            address=host_config["address"],
            host_user=host_config["host_user"],
            password=host_config["password"], 
            port=50051 
        )

        # create host
        #add_host_response = api_instance.add_host(host)
        #logging.info('add host', add_host_response)
        # Get hosts list
        host_list = api_instance.list_hosts()

        # TODO host id should me form add - using the list for testing
        host_id = host_list[0].id
        def get_host():
            return api_instance.get_host(host_id)

        host = get_host()

        # installing
        install_host = qarax.InstallHost(local_node_path=node_config['local_node_path'],
        fcversion='v0.21.1')
        install_response = api_instance.install_host(host_id, install_host=install_host)
        logging.info('%s %s', 'installing host', install_response)

        # check for installation result
        poll_status(get_host)

        health_response = api_instance.health_check(host_id)
        logging.info('%s %s', 'health check', health_response)

        return host_id

    except (ApiException, Exception) as e:
        logging.error("Exception when calling HostsApi %s\n" % e)
        exit(-1)


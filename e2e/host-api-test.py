import qarax
from qarax import Host
from qarax import Configuration
from qarax.rest import ApiException
import bootstrap as bs
import sys
import time
from configparser import ConfigParser

# Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

# Get bootstrap configuration path
bs_config = config_object['booststrap']

bs_host = bs.bootstrap(bs_config['script_path'],bs_config['cache_path'])

conf = Configuration()
conf.host= 'http://localhost:8000'

api_instance = qarax.HostsApi(qarax.ApiClient(conf))
host = Host(
    name='hostoTest',
    address=bs_host["address"],
    host_user=bs_host["host_user"],
    password=bs_host["password"], 
    port=50051 
)

try:
    # Create new host
    add_host_response = api_instance.add_host(host)
    print("add host",add_host_response)
except ApiException as e:
    print("Exception when calling HostsApi->add_host: %s\n" % e)
    exit(-1)

try:
    # Get hosts list
    host_list = api_instance.list_hosts()
    print("Host list",host_list)
except ApiException as e:
    print("Exception when calling HostsApi->list_hosts: %s\n" % e)
    exit(-1)

host_id = host_list[0].id

try:
    # Get host by ID
    host = api_instance.get_host(host_id)
    print("Get by Id",host)
except ApiException as e:
    print("Exception when calling HostsApi->get_host: %s\n" % e)
    exit(-1)

host_config = config_object['HostAPI']
install_host = qarax.InstallHost(local_node_path=host_config['node'],
fcversion='v0.21.1') # InstallHost |  (optional)

try:
    # Install qarax node on host
    install_response = api_instance.install_host(host_id, install_host=install_host)
    print(install_response)
except ApiException as e:
    print("Exception when calling HostsApi->install_host: %s\n" % e)
    exit(-1)

# need to keep polling host until status is up
# set timer
timer = time.time()
timeout = 20 #secs
print('starting polling for host status')
while host.status != 'Up':
    try:
        # Get host by ID
        if (time.time() > timer + timeout):
            raise Exception("installing time passed")
        time.sleep(5)
        host = api_instance.get_host(host_id)
        print("host status is",host.status)
    except (ApiException, Exception) as e:
        print("Exception when calling HostsApi->get_host: %s\n" % e)
        exit(-1)

# Health check
try:
    # Host health check
    health_response = api_instance.health_check(host_id)
    print(health_response)
except ApiException as e:
    print("Exception when calling HostsApi->health_check: %s\n" % e)
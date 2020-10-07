import qarax
from qarax import Host
from qarax import Configuration
import bootstrap as bs
import sys

bs_host = bs.bootstrap('/home/dag/Development/rust/qarax/e2e/','/home/dag/Development/rust/qarax/e2e/.cache')

conf = Configuration()
conf.host= 'http://localhost:8000'

api_instance = qarax.HostsApi(qarax.ApiClient(conf))
body = Host(
    name='hostoTest',
    address=bs_host["address"],
    host_user=bs_host["host_user"],
    password=bs_host["password"], 
    port=50051 
)

# try:
#     # Create new host
#     host_id = api_instance.hosts_post(body)
# except Exception as e:
#     print("Exception when calling HostsApi->hosts_post: %s\n" % e)
#     sys.exit(-1)

try:
    #Get hosts list
    api_response = api_instance.list_hosts()
    print("api response " + str(api_response))
except Exception as e:
    print("Exception when calling HostsApi->hosts_get: %s\n" % e)

try:
    # Get host by ID
    api_response_host = api_instance.get_host(api_response[0].id)
    print(api_response_host)
except Exception as e:
    print("Exception when calling HostsApi->hosts_host_id_get: %s\n" % e)



# Add host to qarax db - returns db id
# Get host id

# Get host list - check fot the added ID
# Get host details - check by name and adress

# call Install qarax node on host
# get host details and check the host status is up

# call healthcheck
# id in url

# Create storage
# Get storage id

# call get list and check storage id included

# call create kernel - get id
# returns kernel id

# Get kernel storage id
# check if the same id as storage added

# call create drive - get id
# returns drive id

# call get drive - look for id is included

# add vm
# attach drive
# get vm details
# get vm drive

# start vm
# get details - get vm ip
# ping ip
# stop vm
# ping ip - should be not responding

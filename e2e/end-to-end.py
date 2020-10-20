import qarax
from qarax import Configuration
import bootstrap as bs
from configparser import ConfigParser
from host_api_test import hosts_api

# Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

# bootstrap
# Get bootstrap configuration path
bs_config = config_object['booststrap']
bs_host = bs.bootstrap(bs_config['script_path'],bs_config['cache_path'])

# API instance
conf = Configuration()
conf.host= 'http://localhost:8000'
api_client= qarax.ApiClient(conf)


# Host API
host_id = hosts_api(api_client, bs_host, config_object['node'])
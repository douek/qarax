import sys
import subprocess
import paramiko
import time
import requests
import os
import logging


USER = "root"
PASSWORD = "fedora"
PORT = 22

IMG_BUCKET_URL="https://s3.amazonaws.com/spec.ccfc.min/img"
KERNEL = IMG_BUCKET_URL + "/hello/kernel/hello-vmlinux.bin"
DRIVE = IMG_BUCKET_URL + "/hello/fsfiles/hello-rootfs.ext4"

def create_host(path='.'):
   # The script already handles the check if already exists
   logging.info("Creating host")
   process = subprocess.run([f'{path}/create_test_vm.sh'],stdout=subprocess.PIPE)
   logging.info(process.stdout)

def run_host(path='.'):
    logging.info("Starting host")
    process = subprocess.run([f'{path}/start_vm.sh'], stdout=subprocess.PIPE)
    logging.info(process.stdout)

def get_ip():
    # set timer
    timer = time.time()
    timeout = 20 #secs
    ip = get_ip_of_host()
    while ip == '':
        # checking for time out
        if (time.time() > timer + timeout):
            raise Exception("Could not find ip")
        time.sleep(5)
        ip = get_ip_of_host()
    return ip

def get_ip_of_host():
    command = "virsh domifaddr --domain fchost | grep vnet0 | tr -s '[:blank:]' | awk '{ print $4 }'"
    ps = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    ip = output.decode("utf-8").split('/')[0]
    logging.info("ip %s", ip)
    return ip

def check_ssh(ip):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port=PORT, username=USER, password=PASSWORD)
        return True
    except Exception as e:
        logging.error(e)
        raise Exception("Could not connect to host with ssh")

def get_drive(path='./.cache'):
    if os.path.isfile(f'{path}/hello-rootfs.ext4'):
        logging.info('file hello-rootfs.ext4 exists')
    else:
        logging.info("Getting drive from uri: " + DRIVE)
        downloaded_obj = requests.get(url=DRIVE)
        with open(f'{path}/hello-rootfs.ext4', 'wb') as file:
            file.write(downloaded_obj.content)

def get_kernel(path='./.cache'):
    if os.path.isfile(f'{path}/hello-vmlinux.bin'):
        logging.info("file hello-vmlinux.bin exists")
    else:
        logging.info("Getting Kernel from uri: " + KERNEL)
        downloaded_obj = requests.get(url=KERNEL)
        with open(f'{path}/hello-vmlinux.bin', 'wb') as file:
            file.write(downloaded_obj.content)

def bootstrap(script_path, cache_path):
    # setting logger configuration
    logging.basicConfig(filename='bootstrap.log',level=logging.INFO)
    # Performing the steps to ensure enviorment is ready for qarax operations
    # (img in .cache folder)
    create_host(script_path)
    run_host(script_path)
    # get ip
    try:
        ip = get_ip()
    except Exception as e:
        logging.error(e.args[0])
        sys.exit(-1)

    logging.info("Host Ip: " + ip)
    # check for ip and ssh
    try:
        if check_ssh(ip):
            logging.info("ssh connect successfuly")
    except Exception as e:
        logging.error(e.args[0])
    # get files for kernel and drive (.cache folder)
    get_drive(cache_path)
    get_kernel(cache_path)

    host = {
        'address' : ip,
        'host_user' : USER,
        'password' : PASSWORD
    }
    return host

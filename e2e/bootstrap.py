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

def create_host():
   # The script already handles the check if already exists
   logging.info("Creating host")
   process = subprocess.run(['./create_test_vm.sh'],stdout=subprocess.PIPE)
   logging.info(process.stdout)

def run_host():
    logging.info("Starting host")
    process = subprocess.run(['./start_vm.sh'], stdout=subprocess.PIPE)
    logging.info(process.stdout)

def check_host_up():
    # set timer
    timer = time.time()
    timeout = 60 #secs
    ip = get_ip_of_host()
    while ip != '':
        # checking for time out
        if (time.time() > timer + timeout):
            logging.error("IP not Found")
            return False
        time.sleep(20)
        ip = get_ip_of_host()
    if ip:
        logging.info("Host Ip: " + ip)
        return check_ssh(ip)

def get_ip_of_host():
    command = "virsh domifaddr --domain fchost | grep vnet0 | tr -s '[:blank:]' | awk '{ print $4 }'"
    ps = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    ip = output.decode("utf-8").split('/')[0]
    return ip

def check_ssh(ip):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port=PORT, username=USER, password=PASSWORD)
        logging.info("SSH connected successfuly")
        return True
    except Exception as e:
        logging.error(e)
        return False

def get_drive():
    if os.path.isfile('.cache/hello-rootfs.ext4'):
        logging.info('file hello-rootfs.ext4 exists')
    else:
        logging.info("Getting drive from uri: " + DRIVE)
        downloaded_obj = requests.get(url=DRIVE)
        with open(".cache/hello-rootfs.ext4", "wb") as file:
            file.write(downloaded_obj.content)

def get_kernel():
    if os.path.isfile('.cache/hello-vmlinux.bin'):
        logging.info("file hello-vmlinux.bin exists")
    else:
        logging.info("Getting Kernel from uri: " + KERNEL)
        downloaded_obj = requests.get(url=KERNEL)
        with open(".cache/hello-vmlinux.bin", "wb") as file:
            file.write(downloaded_obj.content)

check_host_up()

def main():
    # setting logger configuration
    logging.basicConfig(filename='bootstrap.log',level=logging.INFO)
    # Performing the steps to ensure enviorment is ready for qarax operations
    # (img in .cache folder)
    create_host()
    run_host()
    # check for ip and ssh
    if not check_host_up():
        raise Exception(msg="Could not connect to host")
    # get files for kernel and drive (.cache folder)
    get_drive()
    get_kernel()

if __name__ == "__main__":
    main()
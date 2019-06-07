#!/usr/bin/env python
#! python

import requests
import os
import time
import logging 
from tenacity import *

logging.basicConfig( format = '%(asctime)s  %(levelname)-10s %(message)s', filename='/home/pi/rpifiles/upload.log')

@retry(wait=wait_fixed(1), stop=stop_after_attempt(10))

#Checks connection and uploads if connected, if not: disconnects PPP session, resets Nova, reconnects and retries upload. If failed, will run upload-retry.py
def retry_and_stop_after_5_mins():
    try:
        _ = requests.get('http://www.google.com', timeout=10)
        logging.info('Internet is connected, uploading files...')
        os.system('bash /home/pi/rpifiles/RancherCamScripts/upload.sh')
        
    except requests.ConnectionError:
            logging.warning('Upload.py - Internet is STILL down, resetting Modem and running Upload-Retry.py')
    pass
    logging.info('RETRYING NOW')
    os.system('bash /home/pi/rpifiles/RancherCamScripts/upload-retry.sh')
    sleep ( 5 )
    os.system('python /home/pi/rpifiles/RancherCamScripts/upload-retry.py')
    #else:
        #logging.error('!*!*!*!*!ELSE JUST HAPPENED!*!*!*!*!')

#Rechecks connection. If up, uploads files; if down, this moves on to retry_and_stop_after_5_mins
def check_internet():
    url='http://www.google.com/'
    timeout=500
    try:
        os.system('bash /home/pi/rpifiles/RancherCamScripts/modem.sh')
        _ = requests.get(url, timeout=timeout)
        logging.info('Internet is connected, uploading files...')
        os.system('bash /home/pi/rpifiles/RancherCamScripts/upload.sh')
    except requests.ConnectionError:
        logging.warning('Upload.py - No Internet, running failover scripts to recover connection')
        retry_and_stop_after_5_mins()
    return False


check_internet()

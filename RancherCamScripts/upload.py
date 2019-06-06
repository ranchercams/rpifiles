#!/usr/bin/env python
#! python

import requests
import os
import time
import logging 
from tenacity import *

logging.basicConfig( format = '%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s' filename='upload.log', level=logging.WARNING)

@retry(wait=wait_fixed(1),	stop=stop_after_attempt(10))

def retry_and_stop_after_5_mins():
    os.system('bash /home/pi/rpifiles/RancherCamScripts/modem.sh')
    try:
        _ = requests.get('http://www.google.com', timeout=10)
        logging.info('Internet is connected, uploading files...')
        os.system('bash /home/pi/rpifiles/RancherCamScripts/upload.sh')
    except requests.ConnectionError:
            logging.warning('Internet is STILL down, retrying again...')
    pass
    logging.info('RETRYING NOW')
    os.system('bash /home/pi/rpifiles/RancherCamScripts/upload-retry.sh')
    sleep ( 5 )
    os.system('sudo python /home/pi/rpifiles/RancherCamScripts/upload-retry.py')
    else:
        logging.error('!*!*!*!*!ELSE JUST HAPPENED!*!*!*!*!')

def check_internet():
	url='http://www.google.com/'
    timeout=500
    try:
        _ = requests.get(url, timeout=timeout)
        logging.info('Internet is connected, uploading files...')
        os.system('bash /home/pi/rpifiles/RancherCamScripts/upload.sh')
    except requests.ConnectionError:
        logging.warning('Internet is down, retrying now')
        retry_and_stop_after_5_mins()
    return False


check_internet()
#!/usr/bin/env python
#! python

import requests
import os
import time
import logging
from tenacity import *

logging.basicConfig( format = '%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s' filename='upload.log', level=logging.WARNING)

@retry(wait=wait_fixed(1),
		stop=stop_after_attempt(10))
def retry_and_stop_after_1_mins():
    try:
        _ = requests.get('http://www.google.com', timeout=10)
        logging.info('Internet is connected, uploading files...')
	os.system("bash /home/pi/rpifiles/RancherCamScripts/upload.sh")
    except requests.ConnectionError:
        logging.critical('Internet is STILL down, rebooting system and scheduling upload attempt 5 mins from now ...')
	pass
	print("REBOOTING NOW, SCHEDULING NEXT ATTEMPT")
	os.system('echo "python /home/pi/rpifiles/RancherCamScripts/upload.py" | at now + 5 minute')
	sleep ( 5 )
	os.system('sudo reboot')
    else:
        logging.error('!*!*!*!*!ELSE JUST HAPPENED!*!*!*!*!')

def check_internet():
	url='http://www.google.com/'
    timeout=60
    try:
        _ = requests.get(url, timeout=timeout)
        logging.info('Internet is connected, uploading files...')
	os.system("bash /home/pi/rpifiles/RancherCamScripts/upload.sh")
    except requests.ConnectionError:
        logging.warning('Internet is still down, retrying...')
	retry_and_stop_after_1_mins()
    return False


check_internet()
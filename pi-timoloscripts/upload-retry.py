#!/usr/bin/env python
#! python

import requests
import os
import time
import logging
from tenacity import *

logging.basicConfig( format = '%(asctime)s  %(levelname)-10s %(message)s', filename='/home/pi/pi-timolo/upload.log')

@retry(wait=wait_fixed(1), stop=stop_after_attempt(10))

#Checks connection and uploads if connected, if not, schedules a retry +5 mins from now and reboots
def retry_and_stop_after_1_mins():
    try:
        _ = requests.get('http://www.google.com', timeout=10)
        logging.info('Internet is connected, uploading files...')
	os.system("bash /home/pi/pi-timolo/RancherCamScripts/upload.sh")
    except requests.ConnectionError:
        logging.critical('Timolo-Upload-Retry.py - Internet is STILL down, rebooting system and scheduling upload attempt 5 mins from now ...')
	pass
	print("REBOOTING NOW, SCHEDULING NEXT ATTEMPT")
	os.system('echo "python /home/pi/pi-timolo/RancherCamScripts/upload.py" | at now + 5 minute')
	sleep ( 5 )
	os.system('sudo reboot')
    else:
        logging.error('!*!*!*!*!ELSE JUST HAPPENED!*!*!*!*!')

#Rechecks connection. If up, uploads files; if down, this moves on to retry_and_stop_after_1_mins
def check_internet():
    url='http://www.google.com/'
    timeout=60
    try:
        _ = requests.get(url, timeout=timeout)
        logging.info('Internet is connected, uploading files...')
	os.system("bash /home/pi/pi-timolo/RancherCamScripts/upload.sh")
    except requests.ConnectionError:
        logging.warning('Timolo-Upload-Retry.py - Internet is still down, Resetting Modem...')
	retry_and_stop_after_1_mins()
    return False


check_internet()

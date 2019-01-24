#!/usr/bin/env python
#! python

import requests
import os
import time
from tenacity import *


@retry(wait=wait_fixed(1),
		stop=stop_after_attempt(10))
def retry_and_stop_after_5_mins():
    os.system("sh /home/pi/rpifiles/RancherCamScripts/modem.sh")
    try:
        _ = requests.get('http://www.google.com', timeout=10)
        print("Internet is connected, uploading files...")
	os.system("bash /home/pi/rpifiles/RancherCamScripts/upload.sh")
    except requests.ConnectionError:
        print("Internet is STILL down, retrying again...")
	pass
	print("REBOOTING NOW")
	os.system("sudo python /home/pi/rpifiles/RancherCamScripts/errorlogger.py")
	sleep ( 1 )
	os.system('echo "python /home/pi/rpifiles/RancherCamScripts/upload.py" | at now + 5 minute')
	sleep ( 5 )
	os.system('sudo shutdown -r now')
    else:
        print("!*!*!*!*!ELSE JUST HAPPENED!*!*!*!*!")

def check_internet():
    url='http://www.google.com/'
    timeout=500
    try:
        _ = requests.get(url, timeout=timeout)
        print("Internet is connected, uploading files...")
	os.system("bash /home/pi/rpifiles/RancherCamScripts/upload.sh")
    except requests.ConnectionError:
        print("Internet is down, retrying...")
	retry_and_stop_after_5_mins()
    return False


check_internet()
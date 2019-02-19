#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import time
import sys, os
import sigpower
from Hologram.HologramCloud import HologramCloud
from tenacity import *

os.system("sh /home/pi/rpifiles/vedirect/updatevars.sh")
sleep (5)
sys.path.insert(0, '/home/pi/rpifiles/RPI_SSD1306/')


hologram = HologramCloud(dict(), network='cellular')
var_vpv = sigpower.var_vpv
var_batt = sigpower.var_batt
var_bars = sigpower.var_bars
var_op = sigpower.var_op


@retry(wait=wait_fixed(1),
		stop=stop_after_attempt(10))
def retry_and_stop_after_5_mins():
    os.system("sh /home/pi/rpifiles/RancherCamScripts/modem.sh")
    try:
        _ = requests.get('http://www.google.com', timeout=10)
        print("Internet is connected, sending heartbeat...")
	response_code = hologram.sendMessage("Panel is " + str(var_vpv) + " - Batt is " + str(var_batt) + " - Network is " + str(var_op) + " with " + str(var_bars) + " bars of signal", topics=["Gulch"], timeout=10)
	print hologram.getResultString(response_code)
    except requests.ConnectionError:
        print("Internet is STILL down, retrying again...")
	pass
	print("REBOOTING NOW")
	os.system("sudo python /home/pi/rpifiles/RancherCamScripts/errorlogger.py")
	sleep ( 1 )
	os.system('sudo shutdown -r now')
    else:
        print("!*!*!*!*!ELSE JUST HAPPENED!*!*!*!*!")

def check_internet():
    url='http://www.google.com/'
    timeout=500
    try:
        _ = requests.get(url, timeout=timeout)
        print("Internet is connected, sending heartbeat...")
	response_code = hologram.sendMessage("Panel is " + str(var_vpv) + " - Batt is " + str(var_batt) + " - Network is " + str(var_op) + " with " + str(var_bars) + " bars of signal", topics=["Gulch"], timeout=10)
	print hologram.getResultString(response_code)
    except requests.ConnectionError:
        print("Internet is down, retrying...")
	retry_and_stop_after_5_mins()
    return False


check_internet()



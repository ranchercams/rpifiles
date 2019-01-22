#!/usr/bin/env python
#! python


# Import some frameworks
import glob,os
import sys
import custnumber
import time

cust_num = custnumber.custnum


files = glob.glob('/home/pi/rpifiles/RancherCamScripts/' + str(cust_num) + '/*')
for f in files:
    os.remove(f)
time.sleep(10)

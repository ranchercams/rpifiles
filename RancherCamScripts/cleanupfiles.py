#!/usr/bin/env python
#! python


# Import some frameworks
import glob,os
import sys
sys.path.insert(0, '/home/pi/rpifiles/')
from customernumber import custnumber
import time

cust_num = custnumber


files = glob.glob('/home/pi/rpifiles/' + str(cust_num) + '/*')
for f in files:
    os.remove(f)
time.sleep(10)

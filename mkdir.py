#!/usr/bin/env python

import os, sys
import os.path
from os import mkdir
import customernumber

cust_num = customernumber.custnumber

custfolder = os.path.join(cust_num)

os.makedirs(custfolder)

file = open("/home/pi/rpifiles/RancherCamScripts/customernumber.sh","w")

file.write("HOST='indianmeadowshunt.com'\n")
file.write("USER='indianmeadowshfc'\n")
file.write("PASS='Alphatango47!'\n")
file.write("TARGETFOLDER='/public_html/lakecams/" + str(cust_num) + "/'\n")
file.write("SOURCEFOLDER='/home/pi/rpifiles/" + str(cust_num) + "/'\n")

file.close()
#!/usr/bin/env python

import os, sys
import os.path
from os import mkdir
import customernumber
from distutils.dir_util import copy_tree

cust_num = customernumber.custnumber

#copy Files from RancerCam to pi-timolo
copy_tree ("/home/pi/rpifiles/pi-timoloscripts", "/home/pi/pi-timolo/RancherCamScripts")


#Make RancherCam Files for Timed Still Photos
custfolder = os.path.join(cust_num)
os.makedirs(custfolder)
file = open("/home/pi/rpifiles/RancherCamScripts/customernumber.sh","w")

file.write("HOST='indianmeadowshunt.com'\n")
file.write("USER='indianmeadowshfc'\n")
file.write("PASS='Alphatango47!'\n")
file.write("TARGETFOLDER='/public_html/lakecams/" + str(cust_num) + "/'\n")
file.write("SOURCEFOLDER='/home/pi/rpifiles/" + str(cust_num) + "/'\n")

file.close()

#Make/Edit Files for pi-timolo ranchercam uploads
file = open("/home/pi/pi-timolo/RancherCamScripts/customernumber.sh","w")

file.write("HOST='indianmeadowshunt.com'\n")
file.write("USER='indianmeadowshfc'\n")
file.write("PASS='Alphatango47!'\n")
file.write("TARGETFOLDER='/public_html/lakecams/" + str(cust_num) + "/'\n")
file.write("SOURCEFOLDER='/home/pi/pi-timolo/media/'\n")

file.close()




#!/usr/bin/env python

import os, sys
import os.path
import datetime

file = open("/home/pi/rpifiles/RancherCamScripts/upload_errors.log","a+")


open("/home/pi/rpifiles/RancherCamScripts/upload_errors.log","a+").write(datetime.datetime.now().ctime())
open("/home/pi/rpifiles/RancherCamScripts/upload_errors.log", "a+").write('\t'+"Upload failed, rebooting. \n")

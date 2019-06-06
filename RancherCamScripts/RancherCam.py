#!/usr/bin/env python
#! python


# Import some frameworks
import sys
sys.path.insert(0, '/home/pi/rpifiles/')
from customernumber import custnumber
import glob,os
import time
from datetime import datetime
from subprocess import Popen

# Grab the current datetime which will be used to generate dynamic folder names
d = datetime.now()
initYear = "%04d" % (d.year) 
initMonth = "%02d" % (d.month) 
initDate = "%02d" % (d.day)
initHour = "%02d" % (d.hour)
initMins = "%02d" % (d.minute)

cust_num = custnumber

# Define the location where you wish to save files. Set to HOME as default. 
# If you run a local web server on Apache you could set this to /var/www/ to make them 
# accessible via web browser.
folderToSave = "/home/pi/rpifiles/" + str(cust_num)


# Set the initial serial for saved images to 1
fileSerial = 1

# Capture the CURRENT time (not start time as set above) to insert into each capture image filename
hour = "%02d" % (d.hour)
mins = "%02d" % (d.minute)

# Define the size of the image you wish to capture. 
imgWidth = 1296 # Max = 2592 
imgHeight = 972 # Max = 1944

#Name of Camera
cameraName = str(cust_num)


# Capture the image using raspistill. Set to capture with added sharpening, auto white balance and average metering mode
# Change these settings where you see fit and to suit the conditions you are using the camera in
os.system("raspistill -rot 270 -w " + str(imgWidth) + " -h " + str(imgHeight) + " -o " + str(folderToSave) + "/" + str(hour) + ":" + str(mins) + "_" + str(initMonth) + "-" + str(initDate) + "-" +str(initYear) + "_" + str(cust_num) + ".jpg -sh 40 -awb auto -mm average -v -ae 32,0x00,0x8080ff -a 1036 -a " + str(cust_num))

# Increment the fileSerial
fileSerial += 1

#Checks for connection and connects if needed
#os.system("sh modem.sh")
os.system('python /home/pi/rpifiles/RancherCamScripts/upload.py')
    
	
# Uploads the file that was just created
# os.system("sh upload.sh")


# Deletes the contents of the local upload directory for the next run
os.system('python /home/pi/rpifiles/RancherCamScripts/cleanupfiles.py')

#Stops the script
sys.exit("Done!") 

 
    

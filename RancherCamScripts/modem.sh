#!/bin/bash

sleep 10
sudo hologram network disconnect
sleep 5
sudo hologram network connect
sleep 2

wget -q --spider http://google.com

if [ $? -eq 0 ]; then
    echo "Online"
    /home/pi/rpifiles/RancherCamScripts/upload.sh 
else
    echo $(date -u) "Failed to upload, rebooting." $>> /home/pi/rpifiles/RancherCamScripts/uploadfail.log
    sudo reboot
fi
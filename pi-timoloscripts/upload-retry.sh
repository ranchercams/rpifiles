#!/bin/bash

#Tries to cleanly disconnect Nova and close any current PPP session
sudo hologram network disconnect
sleep 5
#Sends AT command to Nova to fully reset
/bin/echo -n -e "at+cfun=15\r\n" > /dev/ttyACM0
sleep 60
#Attempts to reconnect Nova to a fresh ppp session
sudo hologram network connect
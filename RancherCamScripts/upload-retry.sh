#!/bin/bash

sudo hologram network disconnect
sleep 5
/bin/echo -n -e "at+cfun=15\r\n" > /dev/ttyACM0
sleep 60
sudo hologram network connect
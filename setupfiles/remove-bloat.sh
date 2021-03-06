#!/bin/bash


# Remove bloatware
sudo apt-get remove --purge wolfram-engine scratch minecraft-pi sonic-pi oracle-java8-jdk openjdk-8-jre libreoffice* chromium* -y

# Autoremove
sudo apt-get autoremove -y

# Clean
sudo apt-get autoclean -y

# Update
sudo apt-get update

sudo chown -R pi /home/pi/
sudo chmod 777 -R /home/pi/
sleep 5

sudo apt-get install gnome-schedule lftp procps hostapd iproute2 iw haveged dnsmasq iptables ntp build-essential libjpeg8-dev imagemagick libv4l-dev cmake php -y
sleep 2
bash /home/pi/rpifiles/setupfiles/cleanup.sh
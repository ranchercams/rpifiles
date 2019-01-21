#!/bin/bash


# Remove bloatware
sudo apt-get remove --purge wolfram-engine scratch minecraft-pi sonic-pi dillo oracle-java8-jdk openjdk-8-jre libreoffice* geany* chromium* -y

# Autoremove
sudo apt-get autoremove -y

# Clean
sudo apt-get autoclean -y

# Update
sudo apt-get update

sudo chown -R pi /home/pi/
sudo chmod 777 -R /home/pi/

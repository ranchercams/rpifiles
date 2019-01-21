#!/bin/bash


# Install Hologram SDK
sudo curl -L hologram.io/python-install | bash
sudo curl -L hologram.io/python-update | bash

# Install OLED Drivers
cd /home/pi
git clone https://github.com/adafruit/Adafruit_Python_SSD1306
cd Adafruit_Python_SSD1306
sudo python setup.py install

#Install Create_AP
cd /home/pi
git clone https://github.com/oblique/create_ap
cd create_ap
make install

# Set Permissions
sudo chown -R pi /home/pi
sudo chmod -R 777 /home/pi

# Remove Junk Directories and Files
rm -rf /home/pi/Documents
rm -rf /home/pi/Downloads
rm -rf /home/pi/Music
rm -rf /home/pi/Pictures
rm -rf /home/pi/Public
rm -rf /home/pi/Templates
rm -rf /home/pi/Videos
rm -rf /home/pi/MagPi
rm -rf /home/pi/python_games
rm -rf /home/pi/oldconffiles
rm master.zip

# Set Wallpaper
pcmanfm --wallpaper-mode=stretch --set-wallpaper /home/pi/wallpaper.png 

# Install RPi_Cam_Web_Interface
#git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
#./home/pi/RPi_Cam_Web_Interface/install.sh

#Open CRONTAB Editor
crontab -e &
/home/pi/setupfiles/crontab-paste-from-here.txt

#Edit Customer Number info for dependant files
/home/pi/custnumber.py

# Create Directories
python /home/pi/mkdir.py

#Remove cleanup scripts
rm -fr /home/pi/setupfiles
rm /home/pi/mkdir.py

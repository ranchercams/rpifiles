#!/bin/bash


# Install Hologram SDK
sudo curl -L hologram.io/python-install | bash
sleep 2
sudo curl -L hologram.io/python-update | bash
sleep 2

# Install OLED Drivers
cd /home/pi/rpifiles
git clone https://github.com/adafruit/Adafruit_Python_SSD1306
cd Adafruit_Python_SSD1306
sudo python setup.py install
sleep 2

#Install Create_AP
cd /home/pi/rpifiles
git clone https://github.com/oblique/create_ap
cd create_ap
sudo make install
sleep 2

# Install RPI-TIMOLO
curl -L https://raw.github.com/pageauc/pi-timolo/master/source/pi-timolo-install.sh | bash
sleep 2

#Install python dependancies
sudo pip install tenacity
sleep 1
pip install tenacity
sleep 1
sudo pip install interruptingcow
sleep 1
pip install interruptingcow

# Set Permissions
sudo chown -R pi /home/pi
sudo chmod -R 777 /home/pi

# Remove Junk Directories and Files
rm -rf /home/pi/Documents
rm -rf /home/pi/Music
rm -rf /home/pi/Pictures
rm -rf /home/pi/Public
rm -rf /home/pi/Templates
rm -rf /home/pi/Videos
rm -rf /home/pi/MagPi
rm -rf /home/pi/python_games
rm -rf /home/pi/oldconffiles

# Set Wallpaper
pcmanfm --wallpaper-mode=stretch --set-wallpaper /home/pi/rpifiles/wallpaper.png 

#Open CRONTAB Editor
gnome-schedule &
leafpad /home/pi/rpifiles/setupfiles/crontab-paste-from-here.txt

#Edit Customer Number info for dependant files
leafpad /home/pi/rpifiles/customernumber.py

# Create Directories
python /home/pi/rpifiles/mkdir.py
sleep 5

sudo rpi-config
#Remove cleanup scripts
#rm -fr /home/pi/rpifiles/setupfiles
#rm /home/pi/rpifiles/mkdir.py

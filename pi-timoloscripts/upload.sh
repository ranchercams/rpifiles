#!/usr/bin/env bash
sudo systemctl stop ntp
sudo ntpd -q -g
sudo systemctl start ntp

#used to reference FTP params for upload
source /home/pi/pi-timolo/RancherCamScripts/customernumber.sh
 
lftp -f "
open $HOST
user $USER $PASS
lcd $SOURCEFOLDER
set ftp:ssl-allow no
mirror --reverse --verbose $SOURCEFOLDER $TARGETFOLDER
bye
"

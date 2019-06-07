#!/usr/bin/env bash

#used to reference FTP params for upload
source /home/pi/rpifiles/RancherCamScripts/customernumber.sh
 
lftp -f "
open $HOST
user $USER $PASS
lcd $SOURCEFOLDER
set ftp:ssl-allow no
mirror --reverse --verbose $SOURCEFOLDER $TARGETFOLDER
bye
"
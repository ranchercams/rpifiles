#!/bin/bash
HOST='http://wwww.indianmeadowshunt.com'
USER='indianmeadowshfc'
PASS='Alphatango47!'
TARGETFOLDER='/public_html/lakecams/gulch/'
SOURCEFOLDER='/home/pi/gulch/'
 
lftp -f "
open $HOST
user $USER $PASS
lcd $SOURCEFOLDER
set ftp:ssl-allow no
mirror --reverse --verbose $SOURCEFOLDER $TARGETFOLDER
bye
"

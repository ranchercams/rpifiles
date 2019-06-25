#!/bin/bash

crontab -l -u pi | grep -v "RancherCam.sh" | crontab -u pi -

(
crontab -l -u pi
cat <<'EOF'
#ADD CRON JOBS HERE#
1 8,16 * * * /home/pi/rpifiles/RancherCamScripts/RancherCam.sh
EOF
) | crontab -u pi -

#!/bin/bash

python /home/pi/rpifiles/vedirect/vedirect.py --port /dev/ttyUSB0 | grep -oP "'VPV': '\d+'|'V': '\d+'" > /home/pi/vedirect/power.txt
sleep 1
python /home/pi/rpifiles/vedirect/vedirect.py --port /dev/ttyUSB0 | grep -oP "'VPV': '\d+'|'V': '\d+'" > /home/pi/vedirect/power.txt
sudo hologram modem signal > /home/pi/rpifiles/vedirect/sig.py
sleep 1
sudo hologram modem signal > /home/pi/rpifiles/vedirect/sig.py
sleep 1
sudo hologram modem operator > /home/pi/rpifiles/vedirect/op.txt
sleep 1
sed -i -e 's/Signal strength: /var_sig = /g' /home/pi/rpifiles/vedirect/sig.py
sed -i -e 's/Operator: /var_op = /g' /home/pi/rpifiles/vedirect/op.txt
sed -i -e 's/...$//' /home/pi/rpifiles/vedirect/sig.py
sleep 1
python /home/pi/rpifiles/vedirect/signal.py > /home/pi/rpifiles/vedirect/bars.txt
sleep 1
sed -i -e 's/'\''//g' /home/pi/rpifiles/vedirect/power.txt
sed -i -e 's/VPV: /var_vpv = /g' -e 's/V: /var_batt = /g' -e 's/\(.*[0-9]\)\([0-9]\{3\}\)/\1.\2/' /home/pi/rpifiles/vedirect/power.txt
cat /home/pi/vedirect/bars.txt /home/pi/rpifiles/vedirect/power.txt /home/pi/rpifiles/vedirect/op.txt > /home/pi/rpifiles/RPI_SSD1306/sigpower.py
sleep 1

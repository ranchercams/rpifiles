#!/bin/bash

python /home/pi/vedirect/vedirect.py --port /dev/ttyUSB0 | grep -oP "'VPV': '\d+'|'V': '\d+'" > /home/pi/vedirect/power.txt
sleep 1
python /home/pi/vedirect/vedirect.py --port /dev/ttyUSB0 | grep -oP "'VPV': '\d+'|'V': '\d+'" > /home/pi/vedirect/power.txt
sudo hologram modem signal > /home/pi/vedirect/sig.py
sleep 1
sudo hologram modem signal > /home/pi/vedirect/sig.py
sleep 1
sudo hologram modem operator > /home/pi/vedirect/op.txt
sleep 1
sed -i -e 's/Signal strength: /var_sig = /g' /home/pi/vedirect/sig.py
sed -i -e 's/Operator: /var_op = /g' /home/pi/vedirect/op.txt
sed -i -e 's/...$//' /home/pi/vedirect/sig.py
sleep 1
python /home/pi/vedirect/signal.py > /home/pi/vedirect/bars.txt
sleep 1
sed -i -e 's/'\''//g' /home/pi/vedirect/power.txt
sed -i -e 's/VPV: /var_vpv = /g' -e 's/V: /var_batt = /g' -e 's/\(.*[0-9]\)\([0-9]\{3\}\)/\1.\2/' /home/pi/vedirect/power.txt
cat /home/pi/vedirect/bars.txt /home/pi/vedirect/power.txt /home/pi/vedirect/op.txt > /home/pi/RPI_SSD1306/sigpower.py
sleep 1

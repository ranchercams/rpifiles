#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os
os.system("sh /home/pi/rpifiles/vedirect/updatevars.sh")
sys.path.insert(0, '/home/pi/rpifiles/RPI_SSD1306/')
import sigpower
from Hologram.HologramCloud import HologramCloud



hologram = HologramCloud(dict(), network='cellular')
var_vpv = sigpower.var_vpv
var_batt = sigpower.var_batt
var_bars = sigpower.var_bars
var_op = sigpower.var_op


result = hologram.network.connect()
if result == False:
        print ' Failed to connect to cell network'

response_code = hologram.sendMessage("Panel is " + str(var_vpv) + " - Batt is " + str(var_batt) + " - Network is " + str(var_op) + " with " + str(var_bars) + " bars of signal", topics=["Gulch"], timeout=10)
print hologram.getResultString(response_code)

hologram.network.disconnect()

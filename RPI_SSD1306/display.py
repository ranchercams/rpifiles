import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess
from interruptingcow import timeout

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('Montserrat-Light.ttf', 15)
font2 = ImageFont.truetype('fa-light-300.ttf', 28)
font3 = ImageFont.truetype('Montserrat-Medium.ttf', 12)
font_icon_big = ImageFont.truetype('fa-light-300.ttf', 32)
font_text_big = ImageFont.truetype('Montserrat-Medium.ttf', 15)

# Choose Battery icon
def Battery_icon_and_percentage (value):
    if value < 10:
        draw.text((x+46, top+17),       unichr(0xf244),  font=font_icon_big, fill=255)
    elif 10 <= value <= 10.99:
        draw.text((x+46, top+17),       unichr(0xf243),  font=font_icon_big, fill=255)
    elif 11 <= value <= 11.99:
        draw.text((x+46, top+17),       unichr(0xf243),  font=font_icon_big, fill=255)
    elif 12 <= value <= 12.99:
        draw.text((x+46, top+17),       unichr(0xf242),  font=font_icon_big, fill=255)
    elif 13 <= value <= 13.99:
        draw.text((x+46, top+17),       unichr(0xf241),  font=font_icon_big, fill=255)
    elif 13.99 <= value <= 14.50:
        draw.text((x+46, top+17),       unichr(0xf240),  font=font_icon_big, fill=255)
    else:
        draw.text((x+46, top+17),       unichr(0xf377),  font=font_icon_big, fill=255)
    draw.text((x+38 , top),      "Battery",  font=font, fill=255)
    draw.text((x+50, top+46),      str(value),  font=font_text_big, fill=255)

    

#Choose Cellular icon
def Bars_icon (value, var_opp):
    if value==1:
        draw.text((x+45, top+18),       unichr(63116),  font=font2, fill=255)
    elif value==2:
        draw.text((x+45, top+18),       unichr(63117),  font=font2, fill=255)
    elif value==3:
        draw.text((x+45, top+18),       unichr(63118),  font=font2, fill=255)
    elif value==4:
        draw.text((x+45, top+18),       unichr(63119),  font=font2, fill=255)
    elif value==5:
        draw.text((x+45, top+18),       unichr(61458),  font=font2, fill=255)
    else:
        draw.text((x+45, top+18),       unichr(63125),  font=font2, fill=255)
    draw.text((x+5, top), var_opp,  font=font, fill=255)
    draw.text((x+15, top+50), "Signal Bars: ",  font=font, fill=255)
    draw.text((x+105, top+50), str(value), font=font_text_big, fill=255)
	    
try:
    with timeout(60*5, exception=RuntimeError):
        while True:
            # Draw a black filled box to clear the image.
            draw.rectangle((0,0,width,height), outline=0, fill=0)

	    # Open the file "sigpower.py" and take the informations
	    with open("sigpower.py","r") as file:
		    denied = file.read(11)
		    var_batt = float(file.readline())
		    denied = file.read(10)
		    var_vpv = file.readline()
		    denied = file.read(11)
		    var_bars = int(file.readline())
		    denied = file.read(9)
		    var_op = file.readline()

	    #Write data
	    Bars_icon (var_bars,var_op)
	    disp.image(image)
	    disp.display()
	    time.sleep(5)

	    draw.rectangle((0,0,width,height), outline=0, fill=0)
	    Battery_icon_and_percentage (var_batt)
	    disp.image(image)
	    disp.display()
	    time.sleep(5)

	    draw.rectangle((0,0,width,height), outline=0, fill=0)
	    draw.text((x+22, top), "Solar Panel",  font=font, fill=255)
	    draw.text((x+45, top+18),       unichr(62906),  font=font_icon_big, fill=255)
	    draw.text((x+47, top+50), var_vpv, font=font_text_big, fill=255)
	    disp.image(image)
	    disp.display()
	    time.sleep(5)
	    disp.clear()
	    disp.display()


except RuntimeError:
    pass

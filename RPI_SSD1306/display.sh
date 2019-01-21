#!/bin/bash

display(){
	python /home/pi/RPI_SSD1306/display.py
}

until display; do
    echo "'myscript' crashed with exit code $?. Restarting..." >&2
    sleep 15
done
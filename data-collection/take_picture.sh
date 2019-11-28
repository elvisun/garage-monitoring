#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M%S")

fswebcam -S 30 -r 480x240 --no-banner /home/pi/Pictures/data-collection/$DATE.jpg


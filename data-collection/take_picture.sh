#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M%S")

fswebcam -r 244x244 --no-banner /home/pi/Pictures/data-collection/$DATE.jpg


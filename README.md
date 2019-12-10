# garage-monitoring
The repository contains the source code for **Smart garage control with Firebase AutoML and RaspberryPi**.

Here we will explore a creative way to monitor our garage doors - using a Raspberry Pi, Firebase, and a web camera, with some magic using machine learning to send us reminders when we forget to close our garage door. 

## Step 1: data collection

The `take_picture.sh` script that will take a picture and save it.

```
#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M%S")

fswebcam -S 30 -r 480x240 --no-banner /home/pi/Pictures/data-collection/$DATE.jpg
```

Then we set up a cron task using `crontab -e` to run this script every 5 mintue.

```
*/5 * * * * bash ~/Documents/github/garage-monitoring/data-collection/take_picture.sh 2>&1
```

We can also upload all pictures to a Google Cloud Storage bucket every 30 minute.

```
*/30 * * * * gsutil -m cp -r /home/pi/Pictures/data-collection/ gs://garage-door-training-data
```


## Step 2: Train the model with Firebase AutoML
Refer to the article for details.

## Step 3: Using the model
First we setup another cron task to run `get_live_view.sh`, which take a picture every minute.

```
*/5 * * * * bash ~/Documents/github/garage-monitoring/get_live_view.sh 2>&1
```

Then we run the `app.py` script which uses this picture to determine if our garage doors are closed, and send us an SMS reminder if they are not.


## Appendix 
### Installing tensorflow 2.0 on Raspberry pi

If `pip3 install tensorflow` doesn't correctly install tensorflow, try to following:

```
$ sudo apt-get install -y libhdf5-dev libc-ares-dev libeigen3-dev
$ sudo pip3 install keras_applications==1.0.8 --no-deps
$ sudo pip3 install keras_preprocessing==1.1.0 --no-deps
$ sudo pip3 install h5py==2.9.0
$ sudo apt-get install -y openmpi-bin libopenmpi-dev
$ sudo apt-get install -y libatlas-base-dev
$ pip3 install -U --user six wheel mock
$ sudo pip3 uninstall tensorflow
$ sudo -H pip3 install tensorflow-2.0.0-cp37-cp37m-linux_armv7l.whl

【Required】 Restart the terminal.

```

For detail see [this](https://github.com/PINTO0309/Tensorflow-bin) repo.



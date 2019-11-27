# garage-monitoring
Automl Vision to monitor garage

## Installing tensorflow 2.0 on Raspberry pi

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

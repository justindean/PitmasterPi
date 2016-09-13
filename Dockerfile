# raspian wheezy based docker image with most gpio/python packages used as a good source to start from.
FROM mitchtech/rpi-gpio-python

# add in source repo for wheezy
RUN echo "deb http://mirrordirector.raspbian.org/raspbian/ wheezy main contrib non-free rpi" >> /etc/apt/sources.list 

# install i2c and smbus for access to gpio hw/bus by temp controller.  xively and dweepy used for logging temp data to cloud
RUN apt-get update && apt-get install -qy \
    vim \
    i2c-tools \
    python-smbus \
    git \
&& pip install \
    xively-python \
    dweepy

RUN git clone https://github.com/justindean/PitmasterPi.git  

WORKDIR "PitmasterPi/"

RUN git pull

#install and initialize the temp controller as you HAVE to do it with priv access which you can't do at build time with docker build. Starts BBQ smoker with a temp of 225.
CMD ./temperature_controller_install && ./temperature_controller_init && ./PitmasterPi-v2.py 225


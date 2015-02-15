# Introduction


## About

The Python-HIH6130 library is a python wrapper around the python-smbus library for easy communication to the [Honeywell HIH6130][1] relative humidity and temperature sensor.


## Project layout

    setup.py 	   	# Setup file for installation
    LICENSE.txt 	# License information
    README.md 		# Readme file
    HIH6130/
        io.py  # Contains all functions/classes

## Installation

    >>> wget https://github.com/dhhagan/python-hih6130/archive/master.zip
    >>> unzip master.zip
    >>> python3 python-hih6130/setup.py install

## Getting Started

    >>> from HIH6130.io import HIH6130
    >>> rht = HIH6130()
    >>> rht.read()
    >>> print ("Temp: {0}\tRH: {1}".format(rht.t, rht.rh))

[1]: http://www.digikey.com/product-detail/en/HIH6130-021-001/480-3651-1-ND/2704704?WT.srch=1&WT.medium=cpc&WT.mc_id=IQ62057691-VQ2-g-VQ6-53963505795-VQ15-1t1-VQ16-c

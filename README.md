# python-hih6130
Python Library for connecting to/using the Honeywell HIH6130 relative humidity and temperature sensor to the Raspberry Pi.

## Dependencies

1. `python-smbus`
2. `i2c-tools`

## Installation

1. Download the .zip or clone the repo onto your RPi
2. Unzip the folder
3. Run `sudo python setup.py install`

## License

This library is listed under the MIT license.

## Documentation

Check out the [full docs](http://dhhagan.github.io/python-hih6130/)!

### Sample Script

    from HIH6130.io import HIH6130
    
    rht = HIH6130()
    rht.read()
    print ("Timestamp: {0}\tRH: {1}%\tTemp: {2} degC".format(rht.timestamp, rht.rh, rht.t))

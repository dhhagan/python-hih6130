# python-hih6130
Python Library for connecting to/using the Honeywell HIH6130 relative humidity and temperature sensor.

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

Check the wiki for full documentation on the API.

### Sample Script

    from HIH6130.io import HIH6130
    
    rht = HIH6130()
    rht.read()
    print "Timestamp: %s \t RH: %5.2f \t Temp. %5.2f " % (rht.timestamp.strftime("%m-%d-%Y %H:%M:%S"), rht.rh, rht.t) 

## HIH6130

To read from the HIH6130 relative humidity and temperature sensor, you must first initiate an instance of the class. You can read from multiple sensors, as long as each sensor has a unique address.The default address from Honeywell is `0x27`. I believe you must contact them to get sensors with other addresses.

## The HIH6130 Class Object

### Attributes

|  | |
|--------:|:-----|
| **address:** |*int*, contains the i2c address of the sensor|
| **bus:** |*int*, contains the i2c bus being used|
| **status:** |*int*, currently not used but signals the status of the sensor|
| **rh:** |*float*, contains the relative humidity at last measured point with units of %RH|
| **r:** |*float*,contains the last measured temperature with units of degrees celcius|
| **timestamp:** |*datetime.datetime object*, contains the timestamp of the measurement|
| **_buffer:** |*private*|

### Methods

|  | |
|--------:|:-----|
| **read():** | reads from the sensor via i2c and updates the relative humidity, temperature, and timestamp of the measurement. |

### Creating a new HIH6130 Class Object

To create a new instance of the HIH6130 class object, no arguments are required. However, this assumes the default address of `0x27`.

    from HIH6130.io import HIH6130
    rht = HIH6130()

You can also pass a bus argument to specify which i2c bus to use. If no bus argument is passed the module will check to see if bus 0, 1, or 2 exist and use the first one it finds.

    from HIH6130.io import HIH6130
    rht = HIH6130(bus=0)

#### Arguments

|  | |
|--------:|:-----|
| **address:** | *optional*, the default address is 0x27. Check with Honeywell or your technical documentation if otherwise noted. |
| **bus:** | *optional*, the module will use the first bus it can find if this argument is not set.
#### Returns

Returns a HIH6130 object if nothing goes wrong. If an error arrises, an IOError is raised.

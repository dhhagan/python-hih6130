# Continuous Sampling

More often than not, you will be interested in continuously sampling relative humidity and temperature data, rather than just taking a single measurement. This library makes this task very simple. 

    # import libraries
    from HIH6130.io import HIH6130
    import time

    # Create an instance of the HIH6130 class at the default address
    rht = HIH6130()

    while True:
        rht.read()
        print ("RH: {0}\tT: {1}".format(rht.rh, rht.t))
        time.sleep(1)


# Logging Data

Logging data is very similar to the above example for continuous measurements. Simply set up your file for logging and then write to the file rather than printing.

    from HIH6130.io import HIH6130
    import time
    import datetime

    rht = HIH6130()

    now = datetime.datetime.now()
    filename = "rht-data-{0}-{1}-{2}.csv".format(now.year, now.month, now.day)

    with open(filename, "w") as logfile:
        logfile.write("Timestamp,RH (%),T (degC)")

        while True:
            try:
	            rht.read()
	            logfile.write("{0},{1},{2}".format(datetime.datetime.now(),
	             	rht.rh, rht.t))
	            time.sleep(5)
	        except KeyboardInterrupt:
	            logfile.close()
import smbus
from datetime import datetime
import sys
import warnings

__all__ = ['HIH6130']


class HIH6130:
	def __init__(self, address = 0x27):
		self.address = address
		self.status = None
		self.rh = None
		self.t = None
		self.buffer = None
		self.timestamp = None
		
		try:
			self.i2c = smbus.SMBus(1)
		except:
			sys.exit("Could not start SMBus.")
		

		return

	def read(self):
		'''
			read from the I2C bus at address defined above.
		'''
		
		try:
			self.buffer = self.i2c.read_i2c_block_data(self.address, 0, 4)
		except:
			sys.exit("Could not read from i2c bus.")
		

		# Set the timestamp for the measurement
		self.timestamp = datetime.utcnow()

		#Set the status of the sensor
		self.status = self.buffer[0] >> 6 & 0x03

		# Set the RH reading
		self.rh = round(((self.buffer[0] & 0x3f) << 8 | self.buffer[1]) * 100.0 / (2**14 - 1), 2)

		# Set the T reading
		self.t = round((float((self.buffer[2] << 6) + (self.buffer[3] >> 2)) / (2**14 - 1)) * 165.0 - 40, 2)

		return
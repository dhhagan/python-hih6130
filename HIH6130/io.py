import smbus, os
from datetime import datetime

__all__ = ['HIH6130']


class HIH6130:
	''' HIH6130() returns an instance of the RHT sensor with default address of 0x27. '''
	def __init__(self, address = 0x27, bus=None):
		self.address = address
		self.status = None
		self.rh = None
		self.t = None
		self._buffer = None
		self.timestamp = None

		if bus is None:
			for b in range(0,3):
				path = '/dev/i2c-' + str(b)
				try:
					# throws OSError if it dosn't exist
					s = os.stat(path)
					bus = b
					break
				except:
					pass
		# still not found it?
		if bus is None:
			# default to 1, will fail but nothing we can do.
			bus = 1
		self.bus = bus
		
		try:
			self.i2c = smbus.SMBus(self.bus)
		except:
			raise IOError("Could not find i2c device.")

		return

	def read(self):
		''' updates rh, t, and timestamp for the HIH6130 instance '''
		try:
			self._buffer = self.i2c.read_i2c_block_data(self.address, 0, 4)
		except:
			raise IOError("Could not read from i2c device located at %s." % self.address )
		
		self.timestamp = datetime.now()
		self.status = self._buffer[0] >> 6 & 0x03
		self.rh = round(((self._buffer[0] & 0x3f) << 8 | self._buffer[1]) * 100.0 / (2**14 - 1), 2)
		self.t = round((float((self._buffer[2] << 6) + (self._buffer[3] >> 2)) / (2**14 - 1)) * 165.0 - 40, 2)

		return
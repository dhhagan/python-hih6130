'''
	Python library for the HIH6130 RHT sensor from Honeywell

	Written by David H Hagan
	February 2015
	Contact: david@davidhhagan.com
'''

# /HIH6130/setup.py

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(name='HIH6130',
      version='0.0.6',
      description='Python library for interacting with the Honeywell HIH6130 RHT sensor.',
      url='http://github.com/dhhagan/python-hih6130',
      author='David H Hagan',
      author_email='david@davidhhagan.com',
      license='MIT',
	  keywords=['HIH6130', 'relative humidity', 'temperature'],
      packages=['HIH6130',
			],
	  install_requires=[
	  ],
      zip_safe=False)
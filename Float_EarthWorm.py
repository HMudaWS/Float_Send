import logging, PyEW
import time as tiempo
import numpy as np
import struct
import serial

PuertoSerie = serial.Serial('/dev/ttyUSB0', 9600)
tiempo.sleep(1)

logging.getLogger().addHandler(logging.StreamHandler())
MyModule = PyEW.EWModule(1001, 168, 255, 30.0, False)
MyModule.add_ring(1001)
wave = MyModule.get_wave(0) 
MyModule.add_ring(1004)

while True :
	
	sArduino = PuertoSerie.read(4)
	mud, = struct.unpack('<f',sArduino)
	a = np.array([mud])
	
	mywave =  {
	'station': 'MUDA',
	'network': 'UV',
	'channel': 'LK',
	'location': '01',
	'nsamp': 1,
	'samprate': 1,
	'startt': tiempo.mktime(tiempo.gmtime()),
	'datatype': 'i4',
    'data': a
	}
	
	MyModule.put_wave(1, mywave)
	#print (mywave)
	print (a)
	tiempo.sleep(1)
	pass  
  

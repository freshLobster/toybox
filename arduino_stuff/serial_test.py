'''
written by: Aidan Seine
aidanseine@gmail.com
'''
# import the serial library
import serial
# time library for delay
import time
# open the serial port that your arduino 
# is connected to and set the baud rate.
ser = serial.Serial("/dev/ttyACM0", 9600)
#blink function
def blink():
	# working on this, but basically this
	# turns on pin 13 (still working on
	#multiple character reading in arduino)
	ser.write(';')
	# delay one second
	time.sleep(1)
	# turn off
	ser.write(';')
	time.sleep(1)
# blink twice
for i in range(0, 3):
	blink()
# close the port and end the program
ser.close()

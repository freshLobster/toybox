'''
written by: Aidan Seine
aidanseine@gmail.com
displays use of my protocol
to be used with my arduino 
sketch that interprets it.
commands consist of:
mode pin @ (power #)

modes are read and write (r and w)
pin is an int followed by @
power is an int followed by #
power is only used for write and
won't do anything if used with read.

example command:
w13@255#

this command is equivalent to
pinMode(13, OUTPUT); 
analogWrite(13, 255);
in arduino code. 
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
	# uses protocol to turn on pin 13 at 5v
	ser.write('w13@255#')
	# delay one second
	time.sleep(1)
	# turn off
	ser.write('w13@0#')
	time.sleep(1)
# blink twice
for i in range(0, 3):
	blink()
# close the port and end the program
ser.close()

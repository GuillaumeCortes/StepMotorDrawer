import RPi.GPIO as GPIO

import time
import threading

seq = [[1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
	[1,0,0,1]]

seqReverse = [[1,0,0,1],
	[0,0,0,1],
	[0,0,1,1],
	[0,0,1,0],
	[0,1,1,0],
	[0,1,0,0],
	[1,1,0,0],
	[1,0,0,0]]

def moveMotor(motor, steps):
	if int(steps) < 0:
		for i in range(-int(steps)):
	  		for halfstep in range(8):
	    			for pin in range(4):
	      				GPIO.output(motor[pin], seqReverse[halfstep][pin])
            				time.sleep(0.001)
	else:
		for i in range(int(steps)):
		# SPIN #
	  		for halfstep in range(8):
			# 8 steps for one revolution of the core gear #
	    			for pin in range(4):
	      				GPIO.output(motor[pin], seq[halfstep][pin])
	    				time.sleep(0.001)

if __name__ == '__main__':

	GPIO.setmode(GPIO.BOARD)

	ControlPinLeft = [8,16,18,22] # pins connected to motor 1 #
	ControlPinRight = [11,13,15,21] # pins connected to motor 2 #

	for pin in ControlPinLeft:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,0)

	for pin in ControlPinRight:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,0)

	nsteps_right = raw_input("How many steps on right motor ? :)  ")
	nsteps_left = raw_input("How many steps on left motor ? :)  ")

	t_right = threading.Thread(target=moveMotor, args=(ControlPinRight, nsteps_right,))
	t_left = threading.Thread(target=moveMotor, args=(ControlPinLeft, nsteps_left,))
	t_right.start()
	t_left.start()
	t_right.join()
	t_left.join()

	GPIO.cleanup()


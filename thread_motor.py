import time
import threading
import RPi.GPIO as GPIO

from drawer import Drawer
from step_motor import StepMotor

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
					GPIO.output(motor.controlPin[pin], seqReverse[halfstep][pin])
					time.sleep(0.0005)
	else:
		for i in range(int(steps)):
		# SPIN #
			for halfstep in range(8):
			# 8 steps for one revolution of the core gear #
				for pin in range(4):
					GPIO.output(motor.controlPin[pin], seq[halfstep][pin])
					time.sleep(0.0005)

if __name__ == '__main__':

	GPIO.setmode(GPIO.BOARD)

	ControlPinLeft = [8,16,18,22] # pins connected to motor 1 #
	ControlPinRight = [11,13,15,21] # pins connected to motor 2 #

	motorRight = StepMotor('R', ControlPinRight, 0, 0)
	motorLeft = StepMotor('L', ControlPinLeft, 0, 0)

	drawer = Drawer(100, 80, (10,10))
	drawer.print_config();

	nsteps_right = raw_input("How many steps on right motor ? :)  ")
	nsteps_left = raw_input("How many steps on left motor ? :)  ")

	t_right = threading.Thread(target=moveMotor, args=(motorRight, nsteps_right,))
	t_left = threading.Thread(target=moveMotor, args=(motorLeft, nsteps_left,))
	t_right.start()
	t_left.start()
	t_right.join()
	t_left.join()

	GPIO.cleanup()


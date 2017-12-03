import sys
import time
import threading
import RPi.GPIO as GPIO

from drawer import Drawer
from step_motor import StepMotor

if __name__ == '__main__':

	filename = sys.argv[1]

	GPIO.setmode(GPIO.BOARD)

	#motor_left = StepMotor('L', [8,16,18,22])
	#motor_right = StepMotor('R', [11,13,15,21])

	#x = raw_input("How many steps on right motor ? :)  ")
	#y = raw_input("How many steps on left motor ? :)  ")
	## move Right Motor for x steps
	#t_right = threading.Thread(target=motor_right.move, args=(x,))
	#t_right.start()
	## move Left Motor for y steps
	#t_left = threading.Thread(target=motor_left.move, args=(y,))
	#t_left.start()
	## Wait for motors to finish their movements
	#t_right.join()
	#t_left.join()

	drawer = Drawer(100, 80, (10,10))
	drawer.print_config();
	drawer.draw_from_commands(filename);

	GPIO.cleanup()


import RPi.GPIO as GPIO

import sys
from math import sqrt, ceil

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

class StepMotor(object):
	controlPin = []
	x = 0
	y = 0
	string_length = 0
	step_size = 5
	on_change = lambda self: None

	def __init__(self, name, controlPin = [], x=0, y=0, string_length=0):
		# Set motor name (L for left, R for right) 
		self.name = name
		# Initialize Raspberry Pi control pins
		self.controlPin = controlPin
		for pin in self.controlPin:
			GPIO.setup(pin,GPIO.OUT)
			GPIO.output(pin,0)
		# Set motor position and string length
		self.x = x
		self.y = y
		self.string_length = string_length

	def move(self, steps):
		if int(steps) < 0:
			for i in range(-int(steps)):
				for halfstep in range(8):
					for pin in range(4):
						GPIO.output(self.controlPin[pin], seqReverse[halfstep][pin])
						time.sleep(0.0005)
		else:
			for i in range(int(steps)):
			# SPIN #
				for halfstep in range(8):
				# 8 steps for one revolution of the core gear #
					for pin in range(4):
						GPIO.output(self.controlPin[pin], seq[halfstep][pin])
						time.sleep(0.0005)

	# def step_forward(self):
	# 	self.string_length += self.step_size
	# 	write('M{name}{direction}{steps}'.format(name=self.name, direction='+', steps=2))
	# 	self.on_change()

	# def step_backward(self):
	# 	self.string_length -= self.step_size
	# 	write('M{name}{direction}{steps}'.format(name=self.name, direction='-', steps=2))
	# 	self.on_change()

	# def change_length(self, l):
	# 	while abs(self.string_length - l) > self.step_size:
	# 		if self.string_length < l:
	# 			self.step_forward()
	# 		elif self.string_length > l:
	# 			self.step_backward()
import RPi.GPIO as GPIO

import sys
from math import sqrt, ceil


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
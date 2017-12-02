from step_motor import StepMotor

class Drawer(object):
	def __init__(self, width, height, margin=(20, 20), step_size=1, max_segment=5):
		# Set dimensions of the drawing board
		self.width = width
		self.height = height
		self.margin = margin
		# Set motor of the drawing boad
		self.motor_left = StepMotor('L')
		self.motor_right = StepMotor('R')
		self.motor_left.step_size = self.motor_right.step_size = step_size
		# self.handlers = []
		# self.add_change_handler(self.update_pen)
		# self.max_segment = max_segment
		self.coords = []
		self.commands = []
		self.pen_down = False

	def print_config(self): # Print onfiguration of the drawing board
		print "Width x Height: " + str(self.width) + " x " + str(self.height)
		print "Margin: " + str(self.margin)
		print "Motors :"
		print str(self.motor_right.name) + " x=" + str(self.motor_right.x) + " y=" + str(self.motor_right.y)
		print str(self.motor_left.name) + " x=" + str(self.motor_left.x) + " y=" + str(self.motor_left.y)

	# def move_to(self, x, y):
	# 	target_strings = self.find_string_lengths(x, y)
	# 	log('From %s to target length %s' % ((self.motor_left.string_length, self.motor_right.string_length), target_strings))
	# 	# threads are used here because each motor must be controlled simultaneously
	# 	t1 = threading.Thread(target=self.motor_left.change_length, args=(target_strings[0],))
	# 	t2 = threading.Thread(target=self.motor_right.change_length, args=(target_strings[1],))
	# 	t1.start()
	# 	t2.start()
	# 	t1.join()
	# 	t2.join()

	# def set_coordinates(self, coords):
	# 	self.coords = self.scale_image(coords)

	# def set_initial_position(self, x, y):
	# 	self.motor_left.string_length, self.motor_right.string_length = self.find_string_lengths(x, y)
	# 	self.update_pen()

	# def move_to_start(self):
	# 	self.move_to(self.coords[0][0], self.coords[0][1])

	# def find_string_lengths(self, x, y):
	# 	a = float(x) - self.motor_left.x
	# 	b = float(x) - self.motor_right.x
	# 	c = float(y) - self.motor_left.y
	# 	motor_left_p = sqrt((a * a) + (c * c))
	# 	motor_right_p = sqrt((b * b) + (c * c))
	# 	return int(motor_left_p), int(motor_right_p)

	# def update_pen(self):
	# 	width = self.motor_right.x - self.motor_left.x
	# 	x, y = find_pen_position(self.motor_left.string_length, self.motor_right.string_length, width)
	# 	self.pen.x = x
	# 	self.pen.y = y

	def pen_down(self):
		log('Set pen down and press enter')
		raw_input()
		self.pen_down = True
		write('PD')

	def pen_up(self):
		log('Lift pen and press enter')
		raw_input()
		self.pen_down = False
		write('PU')

	# def on_change(self):
	# 	for f in self.handlers:
	# 		f()

	# def add_change_handler(self, f):
	# 	self.handlers.append(f)

	def draw(filename):
		# Get commands from filename
		self.read_commands(filename)
		for x, y in self.coords:
			b = XY(x, y)
			previous = XY(self.pen.x, self.pen.y)
			while int(distance(self.pen, b)) > self.max_segment:
				p = point_on_line(self.pen, b, self.max_segment)
				self.move_to(p.x, p.y)
				if self.pen.x == previous.x and self.pen.y == previous.y:
					log('Breaking out of loop')
					break
				previous = XY(self.pen.x, self.pen.y)
			self.move_to(x, y)

	def read_commands(self, filename):
		# Open the commands file
		f = open(filename, 'r')
		# Read lines 2 by 2
		for line in f:
			nextline=f.next()
			print "OK"
			print line
			print nextline
		f.close()

	# def scale_image(self, coords):
	# 	minx = min([p[0] for p in coords])
	# 	maxx = max([p[0] for p in coords])
	# 	miny = min([p[1] for p in coords])
	# 	maxy = max([p[1] for p in coords])
	# 	dx = float(abs(maxx - minx))
	# 	dy = float(abs(maxy - miny))
	# 	cx = (minx + maxx) / 2.0
	# 	cy = (miny + maxy) / 2.0
	# 	sx = (self.width - (self.margin[0] * 2.0)) / dx
	# 	sy = (self.height - (self.margin[1] * 2.0)) / dy
	# 	s = min(sx, sy)
	# 	tx = ((self.width / 2.0) - (cx * s))
	# 	ty = ((self.height / 2.0) - (cy * s))
	# 	return [((x * s) + tx, (y * s) + ty) for x, y in coords]

import RPi.GPIO as GPIO
import time


delay = 0.000001
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
red1_pin = 17
green1_pin = 18
blue1_pin = 22
red2_pin = 23
green2_pin = 24
blue2_pin = 25
clock_pin = 3
a_pin = 7
b_pin = 8
c_pin = 9
#new pin
d_pin = 10
latch_pin = 4
oe_pin = 2

GPIO.setup(red1_pin, GPIO.OUT)
GPIO.setup(green1_pin, GPIO.OUT)
GPIO.setup(blue1_pin, GPIO.OUT)
GPIO.setup(red2_pin, GPIO.OUT)
GPIO.setup(green2_pin, GPIO.OUT)
GPIO.setup(blue2_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(a_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.OUT)
GPIO.setup(c_pin, GPIO.OUT)
#new pin
GPIO.setup(d_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)
GPIO.setup(oe_pin, GPIO.OUT)

screen = [[0 for x in xrange(32)] for x in xrange(32)]

#screen = [[0 for x in xrange(32)] for x in xrange(32)]

def clock(): 
	GPIO.output(clock_pin, 1)
	GPIO.output(clock_pin, 0)

def latch():
	GPIO.output(latch_pin, 1)
	GPIO.output(latch_pin, 0)

def bits_from_int(x):
	a_bit = x & 1
	b_bit = x & 2
	c_bit = x & 4
	d_bit = x & 8
	return (a_bit, b_bit, c_bit, d_bit)

def color_bits_from_int(x):
	a_bit = x & 1
	b_bit = x & 2 
	c_bit = x & 4
	return (a_bit, b_bit, c_bit)

def set_row(row):
	a_bit, b_bit, c_bit, d_bit = bits_from_int(row)
	GPIO.output(a_pin, a_bit)
	GPIO.output(b_pin, b_bit)
	GPIO.output(c_pin, c_bit)
	GPIO.output(d_pin, d_bit)
	
def set_color_top(color):
	red, green, blue = color_bits_from_int(color)
	GPIO.output(red1_pin, red)
	GPIO.output(green1_pin, green)
	GPIO.output(blue1_pin, blue)

def set_color_bottom(color): 
	red, green, blue = color_bits_from_int(color)
	GPIO.output(red2_pin, red)
	GPIO.output(green2_pin, green)
	GPIO.output(blue2_pin, blue)

def refresh():
	for row in range(16): #changed 8 to 32 
		GPIO.output(oe_pin, 1)
		set_color_top(0)
		set_row(row)
		for col in range(32):
			set_color_top(screen[row][col])
			set_color_bottom(screen[row+8][col]) #changed row + 8
			clock()
		latch()
		GPIO.output(oe_pin, 0)
		time.sleep(delay)

def fill_rectangle(x1, y1, x2, y2, color):
	for x in range(x1, x2):
		for y in range(y1, y2):
			screen[y][x] = color

def set_pixel(x, y, color):
	screen[y][x] = color




#set_pixel(31, 12, 1)


#red
#fill_rectangle(0, 0, 12, 12, 1)
#blue
fill_rectangle(0, 0, 32, 32, 2)
#green
#fill_rectangle(15, 0, 19, 7, 7)

for x in range(32):
	for y in range(32):
		print(screen[y][x]),
	print " "



while True:
	refresh()	

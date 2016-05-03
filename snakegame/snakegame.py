
# imports
import pygame as pg
import snake as snk
import food as fd
import sys
import display
import font
import thread
import os, sys, time
import subprocess
import signal

# screen size and game speed
WIDTH      = 30
HEIGHT     = 30
SPEED      = 8
SPEED_TICK = 2
SPEED_INC  = 5
SHORT      = 12
LONG       = 1
CONTROLLER = ""
CONTROLLER2 = ""
file = 'omxplayer Halo (mp3cut.net).mp3'
command = "omxplayer Halo.mp3"
process = subprocess.Popen(command,stdout=subprocess.PIPE, shell = True, preexec_fn=os.setsid)


#================================================================================================#
#                                       Function Definitions                                     #
#================================================================================================#

# check if the snake's head is outside the limits
def inLimits(snake):
	headpos = snake.getHeadPos()
	return not (headpos[0] < 1 or headpos[1] < 1 or headpos[0] >= HEIGHT+1 or headpos[1] >= WIDTH+1)


#================================================================================================#
#                                       Main Game Part                                           #
#================================================================================================#

# initialize pygame, clock for game speed and threads to listen for controller input

CONTROLLER = ""
ID = 0
def listenController(name, delay):
		global CONTROLLER
		dev = os.open("../../../dev/rfcomm0", os.O_RDONLY)
	
		while True:
			CONTROLLER = os.read(dev,1)
	
try:
	thread.start_new_thread(listenController, ("controller1 thread", 4))
except:
	print "unable to create thread"

#displays start screen
font.letter_S(25, 10, 5)
font.letter_N(20, 10, 5)
font.letter_A(15, 10, 5)
font.letter_K(10, 10, 5)
font.letter_E(5, 10, 5)
display.refresh()

CONTROLLER = ""
while CONTROLLER == "":
	display.refresh()

font.letter_S(25, 10, 0)
font.letter_N(20, 10, 0)
font.letter_A(15, 10, 0)
font.letter_K(10, 10, 0)
font.letter_E(5, 10, 0)
display.refresh()
game_loop = True
while game_loop:

	pg.init() 
	clock = pg.time.Clock()

	# we need a snake and something to eat
	snake = snk.snake(WIDTH/2,HEIGHT/2) #coordinates where the first snake starts
	snake2 = snk.snake(WIDTH/2+5, HEIGHT/2+5) #coordinates where the second snake starts
	food = fd.food(0,1,HEIGHT+1,1,WIDTH+1)
	
	# food should not appear where the snake is
	while food.getPos() in snake.getPosList():
		food.__init__(0,1,HEIGHT+1,1,WIDTH+1)
	
	# will increase game speed every 10 times we eat
	eaten = 0
	
	def listenController2(name, delay):
		global CONTROLLER2
		dev = os.open("../../../dev/rfcomm1", os.O_RDONLY)
	
		while True:
			CONTROLLER2 = os.read(dev,1)

	loser = snake2;
	

	font.letter_P(27, 2, 5)
	font.letter_L(22, 2, 5)
	font.letter_A(18, 2, 5)
	font.letter_Y(14, 2, 5)
	font.letter_E(9, 2, 5)
	font.letter_R(5, 2, 5)
	font.letter_S(0, 2, 5) 

	font.number_1(20, 12, 7)
	font.number_2(12, 12, 5)
	one = True	
	two = False
	CONTROLLER = ""
	while CONTROLLER != "z":
		if CONTROLLER == "a" and two:
			font.number_1(20, 12, 7)
			font.number_2(12, 12, 5)
			one = True
			two = False
		if CONTROLLER == "d" and one:
			font.number_1(20, 12, 5)
			font.number_2(12, 12, 7)
			one = False
			two = True
		display.refresh()
	
	font.letter_P(27, 2, 0)
	font.letter_L(22, 2, 0)
	font.letter_A(18, 2, 0)
	font.letter_Y(14, 2, 0)
	font.letter_E(9, 2, 0)
	font.letter_R(5, 2, 0)
	font.letter_S(0, 2, 0) 

	font.number_1(20, 12, 0)
	font.number_2(12, 12, 0)
	
	if process.poll() == 0:
		process = subprocess.Popen(command,stdout=subprocess.PIPE, shell = True, preexec_fn=os.setsid)

	if two:
		try:
			thread.start_new_thread(listenController2, ("controller1 thread", 4))
		except:
			print "unable to create thread"
	#if CONTROLLER == "1":
	if one:
		print CONTROLLER
		running = True
		while running:
		
			display.refresh()
		
			# check crash or move outside the limits
			if not inLimits(snake) or snake.crashed:
				running = False
				loser = snake
				hold = snake.getPosList()		
				for pair in hold:
					display.set_pixel(pair[0], pair[1], 0)
				display.refresh()
			else:
				pair = food.getPos()
				display.set_pixel(pair[0], pair[1], 4)
				display.refresh()
		
				# check if snake eates
				if food.getPos() == snake.getHeadPos():
					#eatsound.play()
					snake.grow()
					# food should not appear where the snake is
					food.__init__(0,1,HEIGHT+1,1,WIDTH+1)
					while food.getPos() in snake.getPosList():
						food.__init__(0,1,HEIGHT+1,1,WIDTH+1)
					eaten += 1
					# increase game speed
					if eaten % SPEED_INC == 0:
						SPEED += SPEED_TICK
		
				# game speed control
				clock.tick(SPEED)
		
				display.refresh()
		
				# get the next input on queue
				actmotdir = snake.getMotionDir()
	
		
				if CONTROLLER == "w" and actmotdir != snk.DOWN:
					snake.setMotionDir(snk.UP)
				elif CONTROLLER == "s" and actmotdir != snk.UP:
					snake.setMotionDir(snk.DOWN)
				elif CONTROLLER == "a" and actmotdir != snk.LEFT:	
					snake.setMotionDir(snk.RIGHT)
				elif CONTROLLER == "d" and actmotdir != snk.RIGHT:
					snake.setMotionDir(snk.LEFT)
				
				#attempt to display the score
				snakeScore = snake.length - 10
				
				display.refresh()
		
				# remove the snake and make movement
				hold = snake.getPosList()
	
				display.refresh()
		
				for pair in hold:
					display.set_pixel(pair[0], pair[1], 2)
				display.refresh()
				#this removes the last value, so the snake stays a constant length
				pair = hold[len(hold)-1]
				display.set_pixel(pair[0], pair[1], 0)
		
				display.refresh()
		
				snake.move()
				display.refresh()
				if CONTROLLER == "p":
					font.letter_P(20, 10, 5)
					font.letter_A(15, 10, 5)
					font.letter_U(10, 10, 5)
					font.letter_S(5, 10, 5)
					font.letter_E(1, 10, 5)
					while CONTROLLER != "c":
						display.refresh()
					font.letter_P(20, 10, 0)
					font.letter_A(15, 10, 0)
					font.letter_U(10, 10, 0)
					font.letter_S(5, 10, 0)
					font.letter_E(1, 10, 0)	
		pair = food.getPos()
		display.set_pixel(pair[0], pair[1], 0)
		display.refresh()

	elif two:
		try:
			thread.start_new_thread(listenController2, ("controller2 thread", 4))
		except:
			print "unable to create thread"
		print CONTROLLER
		# main loop
		running_1 = True
		running_2 = True
		while running_1 or running_2:
		
			display.refresh()
		
			# check crash or move outside the limits
			if not inLimits(snake) or snake.crashed:
				running_1 = False
				loser = snake
				hold = snake.getPosList()
				for pair in hold:
					display.set_pixel(pair[0], pair[1], 0)
				display.refresh()
			if not inLimits(snake2) or snake2.crashed:
				running_2 = False
				loser = snake2
				hold2 = snake2.getPosList()
				for pair in hold2:
					display.set_pixel(pair[0], pair[1], 0)
				display.refresh()

			if running_1 or running_2:
				pair = food.getPos()
				display.set_pixel(pair[0], pair[1], 4)
				display.refresh()
		
				# check if snake eates
				if food.getPos() == snake.getHeadPos() and running_1:
					#eatsound.play()
					snake.grow()
					# food should not appear where the snake is
					food.__init__(0,1,HEIGHT+1,1,WIDTH+1)
					while food.getPos() in snake.getPosList():
						food.__init__(0,1,HEIGHT+1,1,WIDTH+1)
					eaten += 1
					# increase game speed
					if eaten % SPEED_INC == 0:
						SPEED += SPEED_TICK
						
				if food.getPos() == snake2.getHeadPos() and running_2:
					#eatsound.play()
					snake2.grow()
					# food should not appear where the snake is
					food.__init__(0,1,HEIGHT+1,1,WIDTH+1)
					while food.getPos() in snake.getPosList():
						food.__init__(0,1,HEIGHT+1,1,WIDTH+1)
					eaten += 1
					# increase game speed
					if eaten % SPEED_INC == 0:
						SPEED += SPEED_TICK
		
				# game speed control
				clock.tick(SPEED)
		
				display.refresh()
		
				# get the next input on queue
				actmotdir = snake.getMotionDir()
				actmotdir2 = snake2.getMotionDir()
			
				if not running_2:
					running_2 = False
				elif CONTROLLER2 == "w" and actmotdir2 != snk.DOWN:
					snake2.setMotionDir(snk.UP)
				elif CONTROLLER2 == "s" and actmotdir2 != snk.UP:
					snake2.setMotionDir(snk.DOWN)
				elif CONTROLLER2 == "a" and actmotdir2 != snk.LEFT:
					snake2.setMotionDir(snk.RIGHT)
				elif CONTROLLER2 == "d" and actmotdir2 != snk.RIGHT:
					snake2.setMotionDir(snk.LEFT)		
		
				if not running_1:
					running_1 = False
				elif CONTROLLER == "w" and actmotdir != snk.DOWN:
					snake.setMotionDir(snk.UP)
				elif CONTROLLER == "s" and actmotdir != snk.UP:
					snake.setMotionDir(snk.DOWN)
				elif CONTROLLER == "a" and actmotdir != snk.LEFT:	
					snake.setMotionDir(snk.RIGHT)
				elif CONTROLLER == "d" and actmotdir != snk.RIGHT:
					snake.setMotionDir(snk.LEFT)
				
				#attempt to display the score
				snakeScore = snake.length - 10
				snake2Score = snake2.length - 10
				
				display.refresh()
		
				# remove the snake and make movement
				if running_2:
					hold2 = snake2.getPosList()
					for pair in hold2:
						display.set_pixel(pair[0], pair[1], 6)
					display.refresh()
					#this removes the last value, so the snake stays a constant length
					pair = hold2[len(hold2)-1]
					display.set_pixel(pair[0], pair[1], 0)
				if running_1:
					hold = snake.getPosList()
					for pair in hold:
						display.set_pixel(pair[0], pair[1], 2)
					display.refresh()
					#this removes the last value, so the snake stays a constant length
					pair = hold[len(hold)-1]
					display.set_pixel(pair[0], pair[1], 0)
		
				display.refresh()	
		
				if running_2:
					snake2.move()
				if running_1:
					snake.move()

				display.refresh()
				if CONTROLLER == "p":
					font.letter_P(25, 10, 5)
					font.letter_A(20, 10, 5)
					font.letter_U(15, 10, 5)
					font.letter_S(10, 10, 5)
					font.letter_E(5, 10, 5)
					while CONTROLLER != "c":
						display.refresh()
					font.letter_P(25, 10, 0)
					font.letter_A(20, 10, 0)
					font.letter_U(15, 10, 0)
					font.letter_S(10, 10, 0)
					font.letter_E(5, 10, 0)
				if CONTROLLER2 == "p":
					font.letter_P(25, 10, 5)
					font.letter_A(20, 10, 5)
					font.letter_U(15, 10, 5)
					font.letter_S(10, 10, 5)
					font.letter_E(5, 10, 5)
					while CONTROLLER2 != "c":
						display.refresh()
					font.letter_P(25, 10, 0)
					font.letter_A(20, 10, 0)
					font.letter_U(15, 10, 0)
					font.letter_S(10, 10, 0)
					font.letter_E(5, 10, 0)


		pair = food.getPos()
		display.set_pixel(pair[0], pair[1], 0)
		display.refresh()
	
	snakeScore = snake.length - 10
	snake2Score = snake2.length - 10
	score1 = str(snakeScore)
	score2 = str(snake2Score)
	
	font.letter_P(27, 10, 5)
	font.number_1(22, 10, 5)
	x = 12
	i = 0
	while i < len(score1):
		if score1[i] == '0':
			font.number_0(x, 10, 2)
		elif score1[i] == '1':
			font.number_1(x, 10, 2)
		elif score1[i] == '2':
			font.number_2(x, 10, 2)
		elif score1[i] == '3':
			font.number_3(x, 10, 2)
		elif score1[i] == '4':
			font.number_4(x, 10, 2)
		elif score1[i] == '5':
			font.number_5(x, 10, 2)
		elif score1[i] == '6':
			font.number_6(x, 10, 2)
		elif score1[i] == '7':
			font.number_7(x, 10, 2)
		elif score1[i] == '8':
			font.number_8(x, 10, 2)
		elif score1[i] == '9':
			font.number_9(x, 10, 2)
		i = i + 1
		x = x -5 
	if two:
		font.letter_P(27, 20, 5)
		font.number_2(22, 20, 5)
		x = 12
		i = 0
		while i < len(score2):
			if score2[i] == '0':
				font.number_0(x, 20, 6)
			elif score2[i] == '1':
				font.number_1(x, 20, 6)
			elif score2[i] == '2':
				font.number_2(x, 20, 6)
			elif score2[i] == '3':
				font.number_3(x, 20, 6)
			elif score2[i] == '4':
				font.number_4(x, 20, 6)
			elif score2[i] == '5':
				font.number_5(x, 20, 6)
			elif score2[i] == '6':
				font.number_6(x, 20, 6)
			elif score2[i] == '7':
				font.number_7(x, 20, 6)
			elif score2[i] == '8':
				font.number_8(x, 20, 6)
			elif score2[i] == '9':
				font.number_9(x, 20, 6)
			i = i + 1
			#add to the x length 
			x = x - 5

	CONTROLLER = ""
	while CONTROLLER == "":
		display.refresh()

	for x in range(31):
		for y in range(31):
			display.set_pixel(x, y, 0)
	display.refresh()

	CONTROLLER = ""
	loop = True
	font.letter_P(27, 2, 5)
	font.letter_L(22, 2, 5)
	font.letter_A(17, 2, 5)
	font.letter_Y(13, 2, 5)

	font.letter_A(27, 8, 5)
	font.letter_G(22, 8, 5)
	font.letter_A(17, 8, 5)
	font.letter_I(13, 8, 5)
	font.letter_N(8, 8, 5)
	font.question(3, 8, 5)

	font.letter_Y(28, 17, 7)
	font.letter_E(23, 17, 7)
	font.letter_S(18, 17, 7)
	font.letter_N(10, 17, 5)
	font.letter_O(5, 17, 5)

	display.refresh()	
	
	while CONTROLLER != "z":
		if CONTROLLER == "a" and game_loop == False:
			font.letter_Y(28, 17, 7)
			font.letter_E(23, 17, 7)
			font.letter_S(18, 17, 7)
			font.letter_N(10, 17, 5)
			font.letter_O(5, 17, 5)
			game_loop = True
		if CONTROLLER == "d" and game_loop == True:
			font.letter_Y(28, 17, 5)
			font.letter_E(23, 17, 5)
			font.letter_S(18, 17, 5)
			font.letter_N(10, 17, 7)
			font.letter_O(5, 17, 7)
			game_loop = False
		display.refresh()


	font.letter_P(27, 2, 0)
	font.letter_L(22, 2, 0)
	font.letter_A(17, 2, 0)
	font.letter_Y(13, 2, 0)

	font.letter_A(27, 8, 0)
	font.letter_G(22, 8, 0)
	font.letter_A(17, 8, 0)
	font.letter_I(13, 8, 0)
	font.letter_N(8, 8, 0)
	font.question(3, 8, 0)

	font.letter_Y(28, 17, 0)
	font.letter_E(23, 17, 0)
	font.letter_S(18, 17, 0)
	font.letter_N(10, 17, 0)
	font.letter_O(5, 17, 0)

	display.refresh()

# if crashed print "game over" and wait for esc key
clock.tick(LONG)
snakeposlist = loser.getPosList()
blackblock = loser.backblock
for pos in snakeposlist[1:]:
	clock.tick(SHORT)

os.killpg(os.getpgid(process.pid), signal.SIGTERM)


import display

#these define the font
#defining individual letters pixel by pixel
#each letter is a 5x5 square, included a space

def letter_A(y, x, c):
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+2, y+2, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y, c)
	display.set_pixel(x+3, y+3, c)
	display.set_pixel(x+4, y, c)
	display.set_pixel(x+4, y+3, c)

def letter_C(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x, y, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y+3, c)
	display.set_pixel(x+4, y, c)
	display.set_pixel(x+4, y+1, c)
	display.set_pixel(x+4, y+2, c)
	display.set_pixel(x+4, y+3, c)

def letter_E(y, x, c):
	#display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y+3, c)
	#display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+2, y+2, c)
	display.set_pixel(x+3, y+3, c)
	#display.set_pixel(x+4, y, c)
	display.set_pixel(x+4, y+1, c)
	display.set_pixel(x+4, y+2, c)
	display.set_pixel(x+4, y+3, c)

def letter_G(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x, y, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y+3, c)
	display.set_pixel(x+3, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+4, y, c)
	display.set_pixel(x+4, y+1, c)
	display.set_pixel(x+4, y+2, c)
	display.set_pixel(x+4, y+3, c)

def letter_I(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x+1, y+1, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+3, y+1, c)
	display.set_pixel(x+4, y, c)
	display.set_pixel(x+4, y+1, c)
	display.set_pixel(x+4, y+2, c)	

def letter_K(y, x, c):
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y+3, c)
	display.set_pixel(x+4, y+3, c)
	display.set_pixel(x, y, c)
	display.set_pixel(x+1, y+1, c)
	display.set_pixel(x+2, y+2, c)
	display.set_pixel(x+3, y+1, c)
	display.set_pixel(x+4, y, c)

def letter_L(y, x, c):
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y+3, c)
	display.set_pixel(x+4, y+3, c)
	display.set_pixel(x+4, y+2, c)
	display.set_pixel(x+4, y+1, c)
	#display.set_pixel(x+4, y, c)
	

def letter_N(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+3, y, c)
	display.set_pixel(x+4, y, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+1, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y+3, c)
	display.set_pixel(x+4, y+3, c)
	display.set_pixel(x+1, y+3, c)


def letter_O(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y, c)
	display.set_pixel(x+3, y+3, c)
	display.set_pixel(x+4, y, c)
	display.set_pixel(x+4, y+1, c)
	display.set_pixel(x+4, y+2, c)
	display.set_pixel(x+4, y+3, c)

def letter_P(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+2, y+2, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y+3, c)
	display.set_pixel(x+4, y+3, c)

def letter_R(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+2, y+2, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y+3, c)
	display.set_pixel(x+3, y+1, c)
	display.set_pixel(x+4, y+3, c)
	display.set_pixel(x+4, y, c)

def letter_S(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+2, y+2, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y, c)
	display.set_pixel(x+4, y, c)
	display.set_pixel(x+4, y+1, c)
	display.set_pixel(x+4, y+2, c)
	display.set_pixel(x+4, y+3, c)

def letter_T(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x+1, y+1, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+3, y+1, c)
	display.set_pixel(x+4, y+1, c)
	
def letter_U(y, x, c):
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y+3, c)	
	display.set_pixel(x+4, y+3, c)
	display.set_pixel(x, y, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+3, y, c)	
	display.set_pixel(x+4, y, c)
	display.set_pixel(x+4, y+1, c)
	display.set_pixel(x+4, y+2, c)

def letter_Y(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+1, y+2, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+2, y+2, c)
	display.set_pixel(x+3, y+1, c)
	display.set_pixel(x+4, y+1, c)

def question(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+2, y+2, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y+3, c)
	display.set_pixel(x+5, y+3, c)

#deletes letters from screen

def remove_A(y, x, c):
	display.set_pixel(x, y+1, 0)
	display.set_pixel(x, y+2, 0)
	display.set_pixel(x+1, y, 0)
	display.set_pixel(x+1, y+3, 0)
	display.set_pixel(x+2, y, 0)
	display.set_pixel(x+2, y+1, 0)
	display.set_pixel(x+2, y+2, 0)
	display.set_pixel(x+2, y+3, 0)
	display.set_pixel(x+3, y, 0)
	display.set_pixel(x+3, y+3, 0)
	display.set_pixel(x+4, y, 0)
	display.set_pixel(x+4, y+3, 0)

def remove_C(y, x, c):
	display.set_pixel(x, y, 0)
	display.set_pixel(x, y+1, 0)
	display.set_pixel(x, y+2, 0)
	display.set_pixel(x, y+3, 0)
	display.set_pixel(x, y, 0)
	display.set_pixel(x+1, y+3, 0)
	display.set_pixel(x+2, y+3, 0)
	display.set_pixel(x+3, y+3, 0)
	display.set_pixel(x+4, y, 0)
	display.set_pixel(x+4, y+1, 0)
	display.set_pixel(x+4, y+2, 0)
	display.set_pixel(x+4, y+3, 0)

def remove_E(y, x, c):
	display.set_pixel(x, y, 0)
	display.set_pixel(x, y+1, 0)
	display.set_pixel(x, y+2, 0)
	display.set_pixel(x, y+3, 0)
	display.set_pixel(x+1, y+3, 0)
	display.set_pixel(x+2, y+3, 0)
	display.set_pixel(x+2, y+1, 0)
	display.set_pixel(x+2, y+2, 0)
	display.set_pixel(x+3, y+3, 0)
	display.set_pixel(x+4, y, 0)
	display.set_pixel(x+4, y+1, 0)
	display.set_pixel(x+4, y+2, 0)
	display.set_pixel(x+4, y+3, 0)	

def remove_G(y, x, c):
	display.set_pixel(x, y, 0)
	display.set_pixel(x, y+1, 0)
	display.set_pixel(x, y+2, 0)
	display.set_pixel(x, y+3, 0)
	display.set_pixel(x, y, 0)
	display.set_pixel(x+1, y+3, 0)
	display.set_pixel(x+2, y+3, 0)
	display.set_pixel(x+3, y+3, 0)
	display.set_pixel(x+3, y, 0)
	display.set_pixel(x+2, y+1, 0)
	display.set_pixel(x+2, y, 0)
	display.set_pixel(x+4, y, 0)
	display.set_pixel(x+4, y+1, 0)
	display.set_pixel(x+4, y+2, 0)
	display.set_pixel(x+4, y+3, 0)

def remove_I(y, x, c):
	display.set_pixel(x, y, 0)
	display.set_pixel(x, y+1, 0)
	display.set_pixel(x, y+2, 0)
	display.set_pixel(x+1, y+1, 0)
	display.set_pixel(x+2, y+1, 0)
	display.set_pixel(x+3, y+1, 0)
	display.set_pixel(x+4, y, 0)
	display.set_pixel(x+4, y+1, 0)
	display.set_pixel(x+4, y+2, 0)	


def remove_K(y, x, c):
	display.set_pixel(x, y+3, 0)
	display.set_pixel(x+1, y+3, 0)
	display.set_pixel(x+2, y+3, 0)
	display.set_pixel(x+3, y+3, 0)
	display.set_pixel(x+4, y+3, 0)
	display.set_pixel(x, y, 0)
	display.set_pixel(x+1, y+1, 0)
	display.set_pixel(x+2, y+2, 0)
	display.set_pixel(x+3, y+1, 0)
	display.set_pixel(x+4, y, 0)

def remove_L(y, x, c):
	display.set_pixel(x, y+3, 0)
	display.set_pixel(x+1, y+3, 0)
	display.set_pixel(x+2, y+3, 0)
	display.set_pixel(x+3, y+3, 0)
	display.set_pixel(x+4, y+3, 0)
	display.set_pixel(x+4, y+2, 0)
	display.set_pixel(x+4, y+1, 0)
	display.set_pixel(x+4, y, 0)

def remove_N(y, x, c):
	display.set_pixel(x, y, 0)
	display.set_pixel(x+1, y, 0)
	display.set_pixel(x+2, y, 0)
	display.set_pixel(x+3, y, 0)
	display.set_pixel(x+4, y, 0)
	display.set_pixel(x+1, y, 0)
	display.set_pixel(x+2, y+1, 0)
	display.set_pixel(x+1, y+2, 0)
	display.set_pixel(x, y+3, 0)
	display.set_pixel(x+1, y+3, 0)
	display.set_pixel(x+2, y+3, 0)
	display.set_pixel(x+3, y+3, 0)
	display.set_pixel(x+4, y+3, 0)
	display.set_pixel(x+1, y+3, 0)


def remove_O(y, x, c):
	display.set_pixel(x, y, 0)
	display.set_pixel(x, y+1, 0)
	display.set_pixel(x, y+2, 0)
	display.set_pixel(x, y+3, 0)
	display.set_pixel(x+1, y, 0)
	display.set_pixel(x+1, y+3, 0)
	display.set_pixel(x+2, y, 0)
	display.set_pixel(x+2, y+3, 0)
	display.set_pixel(x+3, y, 0)
	display.set_pixel(x+3, y+3, 0)
	display.set_pixel(x+4, y, 0)
	display.set_pixel(x+4, y+1, 0)
	display.set_pixel(x+4, y+2, 0)
	display.set_pixel(x+4, y+3, 0)

def remove_P(y, x, c):
	display.set_pixel(x, y, 0)
	display.set_pixel(x, y+1, 0)
	display.set_pixel(x, y+2, 0)
	display.set_pixel(x, y+3, 0)
	display.set_pixel(x+1, y, 0)
	display.set_pixel(x+1, y+3, 0)
	display.set_pixel(x+2, y, 0)
	display.set_pixel(x+2, y+1, 0)
	display.set_pixel(x+2, y+2, 0)
	display.set_pixel(x+2, y+3, 0)
	display.set_pixel(x+3, y+3, 0)
	display.set_pixel(x+4, y+3, 0)

def remove_R(y, x, c):
	display.set_pixel(x, y, 0)
	display.set_pixel(x, y+1, 0)
	display.set_pixel(x, y+2, 0)
	display.set_pixel(x, y+3, 0)
	display.set_pixel(x+1, y, 0)
	display.set_pixel(x+1, y+3, 0)
	display.set_pixel(x+2, y, 0)
	display.set_pixel(x+2, y+1, 0)
	display.set_pixel(x+2, y+2, 0)
	display.set_pixel(x+2, y+3, 0)
	display.set_pixel(x+3, y+3, 0)
	display.set_pixel(x+3, y+1, 0)
	display.set_pixel(x+4, y+3, 0)
	display.set_pixel(x+4, y, 0)

def remove_S(y, x, c):
	display.set_pixel(x, y, 0)
	display.set_pixel(x, y+1, 0)
	display.set_pixel(x, y+2, 0)
	display.set_pixel(x, y+3, 0)
	display.set_pixel(x+1, y+3, 0)
	display.set_pixel(x+2, y, 0)
	display.set_pixel(x+2, y+1, 0)
	display.set_pixel(x+2, y+2, 0)
	display.set_pixel(x+2, y+3, 0)
	display.set_pixel(x+3, y, 0)
	display.set_pixel(x+4, y, 0)
	display.set_pixel(x+4, y+1, 0)
	display.set_pixel(x+4, y+2, 0)
	display.set_pixel(x+4, y+3, 0)

def remove_T(y, x, c):
	display.set_pixel(x, y, 0)
	display.set_pixel(x, y+1, 0)
	display.set_pixel(x, y+2, 0)
	display.set_pixel(x+1, y+1, 0)
	display.set_pixel(x+2, y+1, 0)
	display.set_pixel(x+3, y+1, 0)
	display.set_pixel(x+4, y+1, 0)

def remove_U(y, x, c):
	display.set_pixel(x, y+3, 0)
	display.set_pixel(x+1, y+3, 0)
	display.set_pixel(x+2, y+3, 0)
	display.set_pixel(x+3, y+3, 0)	
	display.set_pixel(x+4, y+3, 0)
	display.set_pixel(x, y, 0)
	display.set_pixel(x+1, y, 0)
	display.set_pixel(x+2, y, 0)
	display.set_pixel(x+3, y, 0)	
	display.set_pixel(x+4, y, 0)
	display.set_pixel(x+4, y+1, 0)
	display.set_pixel(x+4, y+2, 0)

def remove_Y(y, x, c):
	display.set_pixel(x, y, 0)
	display.set_pixel(x, y+2, 0)
	display.set_pixel(x+1, y, 0)
	display.set_pixel(x+1, y+2, 0)
	display.set_pixel(x+2, y, 0)
	display.set_pixel(x+2, y+1, 0)
	display.set_pixel(x+2, y+2, 0)
	display.set_pixel(x+3, y+1, 0)
	display.set_pixel(x+4, y+1, 0)


def remove_question(y, x, c):
	display.set_pixel(x, y, 0)
	display.set_pixel(x, y+1, 0)
	display.set_pixel(x, y+2, 0)
	display.set_pixel(x, y+3, 0)
	display.set_pixel(x+1, y, 0)
	display.set_pixel(x+2, y, 0)
	display.set_pixel(x+2, y+1, 0)
	display.set_pixel(x+2, y+2, 0)
	display.set_pixel(x+2, y+3, 0)
	display.set_pixel(x+3, y+3, 0)
	display.set_pixel(x+5, y+3, 0)


#they are a 4x5 square

def number_0(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y, c)
	display.set_pixel(x+3, y+3, c)
	display.set_pixel(x+4, y, c)
	display.set_pixel(x+4, y+1, c)
	display.set_pixel(x+4, y+2, c)
	display.set_pixel(x+4, y+3, c)

def number_1(y, x, c):
	display.set_pixel(x, y+1, c)
	display.set_pixel(x+1, y+1, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+3, y+1, c)
	display.set_pixel(x+4, y+1, c)

def number_2(y, x, c):
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+3, y+2, c)
	display.set_pixel(x+4, y, c)
	display.set_pixel(x+4, y+1, c)
	display.set_pixel(x+4, y+2, c)
	display.set_pixel(x+4, y+3, c)

def number_3(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+2, y+2, c)
	display.set_pixel(x+3, y, c)
	display.set_pixel(x+4, y, c)
	display.set_pixel(x+4, y+1, c)
	display.set_pixel(x+4, y+2, c)

def number_4(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+2, y+2, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y, c)
	display.set_pixel(x+4, y, c)

def number_5(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+2, y+2, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y, c)
	display.set_pixel(x+4, y, c)
	display.set_pixel(x+4, y+1, c)
	display.set_pixel(x+4, y+2, c)
	display.set_pixel(x+4, y+3, c)

def number_6(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+2, y+2, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y, c)
	display.set_pixel(x+3, y+3, c)
	display.set_pixel(x+4, y, c)
	display.set_pixel(x+4, y+1, c)
	display.set_pixel(x+4, y+2, c)
	display.set_pixel(x+4, y+3, c)

def number_7(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+3, y, c)
	display.set_pixel(x+4, y, c)

def number_8(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+2, y+2, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y, c)
	display.set_pixel(x+3, y+3, c)
	display.set_pixel(x+4, y, c)
	display.set_pixel(x+4, y+1, c)
	display.set_pixel(x+4, y+2, c)
	display.set_pixel(x+4, y+3, c)

def number_9(y, x, c):
	display.set_pixel(x, y, c)
	display.set_pixel(x, y+1, c)
	display.set_pixel(x, y+2, c)
	display.set_pixel(x, y+3, c)
	display.set_pixel(x+1, y, c)
	display.set_pixel(x+1, y+3, c)
	display.set_pixel(x+2, y, c)
	display.set_pixel(x+2, y+1, c)
	display.set_pixel(x+2, y+2, c)
	display.set_pixel(x+2, y+3, c)
	display.set_pixel(x+3, y, c)
	display.set_pixel(x+4, y, c)


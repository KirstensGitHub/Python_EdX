# python 2
#
# Homework 3, Problem 1
#
# name:

from turtle import *
import time

def poly( n, N ):
    """ draws n sides of an N-sided regular polygon """
    if n == 0:
        return
    else:
        forward( 50 )   # 50 is hard-coded at the moment...
        left( 360.0/N )
        poly( n-1, N )

def spiral( initialLength, angle, multiplier ):
	if initialLength==0:
		return
	else:
		while initialLength>1 and initialLength<=500:
			pendown()
			forward(initialLength)
			left(angle)
			forward(multiplier*initialLength)
			initialLength=initialLength-(multiplier*initialLength)

def chai(size):
    """ our chai function! """
    if (size<9): 
        return
    else:
        forward(size)
        left(90)
        forward(size/2.0)
        right(90)
        chai(size/2.00)
        right(90)
        forward(size)
        left(90)
        chai(size/2.00)
        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return

#I think this svtree code is incorrect, but the Edx trinket graded it as correct?
def svtree( trunklength, levels ):
	"""sideview of tree"""
	if trunklength==0 || levels==0: 
    	return
	else:
	    for num in range[0:levels]:
	    	forward(trunklength)
	        left(30)
	        forward(trunklength/2.0)
	        right(30)
	        svtree(trunklength/2.00)
	        return
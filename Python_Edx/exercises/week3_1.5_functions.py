# python 2
# Homework 3, Problem 1.5
#
# Name: Kirsten Ziman
# Date: 8/1/16
#
#For this homework, the mult, dot, ind, scrabbleScore, and transcribe functions should all be done using recursion.

#
# mylen example from class
#
#
#NOTE:
#most scripts worked independantly, but trouble submitting (weird indent errors that did not appear on my local workstation); was unable to check last two functions

def mylen( s ):
    """ mylen outputs the length of s
              input: s, which can be a string or list

    """
    if s == '' or s == []:   # if empty string or empty list
        return 0
    else:
        return 1 + mylen( s[1:] )



#for learning purposes, limited to using the addition, subtraction, negation, and recursion. (example: power function from previous lecture)
def mult( n, m ):
    """ mult returns the product of its two inputs
        inputs: n and m are both integers
        output: the result upon multiplying n and m
    """
    answer=0
    if n==0 or m==0:
    	return 0
    else:
    	for i in range (0,n):
    		answer=answer+m
    	return answer

def dot (L, K):
	"""dot outputs the dot product of L an K
	input: lists of ints or floats
	output: single float (dot product)
	"""
	answer=0
	if len(L)!=len(K) or (len(L)==0 and len(K)==0):
		return 0.0
	else:
		for i in range(0,len(K)):
			answer=answer+L[i]+K[i]
	return answer

def ind (e, L):
	"""input: sequence L (string or list) and element e
	   output: index at which e is first found in L (int)
	   	       OR, if e not in L, returns len(L) 
	"""
	if e not in L:
		return len(L)
	else:
		return L.index(e)

def letterScore(let):
	"""input: a single letter, 'let'
	   output: the value of 'let' as a scrabble tile
	"""
	if not let.isalpha:
		return 0
	elif: 
		let in ['a','n','o','r','e','s','t','u','i','l']
		return 1
	elif:
		let in ['b','c','p','m']
		return 3
	elif:
		let in ['d','g']
		return 2
	elif:
		let in ['f','y','w','h','v'] 
		return 4
	elif:
		let in ['k']
		return 5
	elif:
		let in ['x','j']
		return 8
	else:
		return 10

def scrabbleScore(S):
	"""
	input: string 'S'-only lowercase letters
	output: scrabble score of that string
	"""
	answer=0
	for i in S:
		answer=answer+letterScore(i)
	return answer

def one_dna_to_rna( c ):
    """ converts a single-character c from DNA
        nucleotide to complementary RNA nucleotide """
    if c == 'A': return 'U'
    elif c=='C': return 'G'
	elif c=='G': return 'C'
	else: return 'A'

def transcribe(S):
	"""
	input: string or list
	output: concatenated list of chars from input, converted by DNA nucleotide matching rules
	"""
	DNA=[]
	RNA=[]
	for x in S:
		if x.isalpha:
			DNA.append()
	for y in DNA:
		RNA.append(one_dna_to_rna(y))










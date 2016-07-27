#task: interactive rock, paper, scissors game


#IMPORTS#
import random

#VARIABLES#
x=('rock', 'paper', 'scissors')
#rps=' '.join(x)

#SCRIPT#
user = raw_input('choose rock, paper, or scissors: ')  
comp = random.choice(x)

if comp == user:
	print 'Tie.'

elif comp == x[1]:
  	if user == x[0]:
  		print 'I win!'
  	else:
  		print 'You win.'

elif comp == x[0]:
  if user == x[2]:
    print 'I win!'
  else: 
    print 'You win.'

else:
	if user == x[1]:
		print 'I Win!'
	else:
		print 'You win.'
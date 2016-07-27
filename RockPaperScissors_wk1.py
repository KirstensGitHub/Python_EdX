#task: fix this code so it accurately reflects a game of rock, paper, scissors


comp = 'rock'
user = 'paper' # this line is changed during the video


if comp == 'paper':
  	if user == 'rock':
  		print 'I win!'
  	else:
  		print 'You win.'

elif comp == 'rock':
  if user == 'scissors':
    print 'I win!'
  elif user == 'paper':
    print 'You win.'

else:

  print 'Tie.'
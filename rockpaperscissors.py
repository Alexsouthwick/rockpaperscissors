//THIS IS A COMMENT FOR ADVANCED SOFTTWARE ENGINEERING
//HELLOOOOOOO


import random
import time
options = ['rock', 'paper', 'scissors']
game_on = True

print('Rock, Paper, Scissors!')
print('\n')
while game_on == True:
	print('To play, enter you answer. To quit, enter q')
	my_answer = random.choice(options)
	answer = input('Enter your answer (rock, paper, scissors): ')
	print('\n')
	if answer in options or answer == 'apache helicopter':
		print('You answered: ' + answer + ' and I answered: ' + my_answer)
		print('\n')
		time.sleep(1.5)
		if answer == my_answer:
			print('It is a tie! Try again')
			print('\n')
			time.sleep(1.5)
		if answer == 'apache helicopter':
			print('You destroyed the competition! You are victorious!')
			print('\n')
			time.sleep(1.5)
		if answer == 'rock' and my_answer == 'scissors' or answer == 'paper' and my_answer == 'rock' or answer == 'scissors' and my_answer == 'paper':
			print('Congratulations! You win!')
			print('\n')
			time.sleep(1.5)
		if my_answer == 'rock' and answer == 'scissors' or my_answer == 'paper' and answer == 'rock' or my_answer == 'scissors' and answer == 'paper':
			print('Oops. You lost. Better luck next time!')
			print('\n')
			time.sleep(1.5)
	elif answer == 'q':
		game_on = False
	else:
		print('Error. Incorrect input')
		print('\n')
	
	

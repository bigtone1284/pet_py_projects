"""=======================================================================================

Guessing Game in Python

by Tony DeFreitas
August 12, 2014

======================================================================================="""
import random, time
	
def guessing_game(number_of_plays = None):
	
	if number_of_plays == None:
	
		print "So here is how the game works: \nI will think of a number and you must try and guess it. \nYou choose the range of numbers from which I'll pick a number from."
		time.sleep(2)
		number_of_plays = 1
	
	min = int(raw_input("Please enter a min and a max number.\n"))
	max = int(raw_input())
	while min == max:
		print "Error--You min and max are the same number.\nPlease try again."
		min = int(raw_input())
		max = int(raw_input())
	
	if min > max:
		min, max = max, min
	mystery_number = random.randint(min, max)
	guess = int(raw_input("Make your first guess!\n"))
	guesses = 1
	floor, ceiling = min, max
	
	while guess != mystery_number:
		if guess < floor or guess > ceiling:
			guess = int(raw_input("Error--Guess out of range.  Try again.\n"))
		else:
			if guess > mystery_number:
				ceiling = guess
				guess = int(raw_input("Lower. Guess again.\n"))
				guesses += 1
			elif guess < mystery_number:
				floor = guess
				guess = int(raw_input("Higher. Guess again.\n"))
				guesses += 1
	if guess == mystery_number:
		print "You got it!"
		time.sleep(1)
		if guesses == 1:
			print "It only took you %d guess!" % guesses
		else:
			print "It took you %d guesses." % guesses
	play_again = raw_input("Do you want to play again? (y/n)\n")
	if play_again == "y":
		number_of_plays += 1
		guessing_game(number_of_plays)
		
	else:
		if number_of_plays == 1:
			print "You played %d time." % number_of_plays
		else:
			print "You played %d times." % number_of_plays
		print "Thanks for playing!"
		
	
def main():
	guessing_game()
	
if __name__ == "__main__":
	main()

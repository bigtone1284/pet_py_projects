"""=======================================================================================

Hangman in Python

by Tony DeFreitas
August 12, 2014

======================================================================================="""
import random, string, re
word_list = ("hangman", "chairs", "backpack", "bodywash", "clothing", "computer", "python", "program", "glasses", "sweatshirt", "sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "suitcase", "knives", "ninjas", "shampoo")
intro = "Welcome to Hangman.\nYou will have 6 guesses to correctly guess the word."

def the_hangman(int):
	hangman_dict = {0: "--------\n|    \n|   \n|  \n|   \n|  \n|\n========",
					1: "--------\n|   |\n|   0 \n|  \n|   \n|  \n|\n========",
					2: "--------\n|   |\n|   0 \n|   |\n|   |\n|  \n|\n========",
					3: "--------\n|   |\n|   0 \n|  /|\n|   |\n|  \n|\n========",
					4: "--------\n|   |\n|   0 \n|  /|\ \n|   |\n|  \n|\n========",
					5: "--------\n|   |\n|   0 \n|  /|\ \n|   |\n|  /\n|\n========",
					6: "--------\n|   |\n|   0 \n|  /|\ \n|   |\n|  / \ \n|\n========"
					}
	print hangman_dict[int]
 
	
def remove_letter(x,string):
	if x in string:
		string = string.replace(x, "")
	else:
		print "You've already guessed %s!  Try again."  % x
	return string

def fill_in_letters(y, string, blanks):
	occurences = []
	if y in string:
		occurences = [m.start() for m in re.finditer(y, string)]
	else:
		print "Sorry, there are no %s's." % y
	for i in occurences:
		blanks = blanks[:i] + string[i] + blanks[i+1:]
	return blanks
		 

def play_again():
	response = raw_input("Do you want to play again? (y/n)\n")
	if response == "y":
		hangman_game("play")
	elif response == "n":
		print "Thanks for playing!"

def hangman_game(no_intro = None):
	
	word = random.choice(word_list)
	if no_intro == None:
		print intro
	wrongs = 0
	dashes = len(word) * "-"
	alphabet = string.ascii_lowercase
	print dashes
	while wrongs < 6 and "-" in dashes:
		the_hangman(wrongs)
		guess = raw_input("Guess a letter or word. ")
		if len(guess) > 1:
			if guess == word:
				break
			else:
				print "Wrong guess!"
				wrongs += 1
		else:		
			dashes = fill_in_letters(guess, word, dashes)
			alphabet = remove_letter(guess, alphabet)
			print dashes
			if guess not in word:
				wrongs += 1
			
			
	if wrongs != 6:
		print "You win!"
		
	else:
		the_hangman(wrongs)
		print "You lose!\nThe word was %s." % word	
	
	play_again()
			
		

def main():
	hangman_game()

if __name__ == "__main__":
	main()

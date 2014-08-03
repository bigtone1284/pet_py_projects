"""
String Reverse

String Reverse takes a string from the user and returns that string reversed.  I starting messing around with main()
if __name__ == '__main__' just to see what each does and how they work.  

"""

def string_reverse(string):
	return string[::-1]

#string_reverse("turn the beat around.")

##def main():
	#word = raw_input("Enter a string.  Get it reversed! ")
	#return string_reverse((word))

if __name__ == '__main__':
	word = raw_input("Enter a string.  Get it reversed! ")
	print string_reverse((word))
	
	#print main()

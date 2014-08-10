"""========================================================================================================================

A python script that creates a multiplcation table of dimension based on the user's input.  

========================================================================================================================"""

import sys
arg1 = sys.argv[1]


def multiplication_table(x):
	x = int(x) + 1
	y = str(x * x)
	for i in range(1,int(x)):
		for j in range(1,int(x)):
			z = str(i * j)
			print ((" ") * (len(y) - len(z)))+ z,
		print "\n"

def main():
	return multiplication_table(arg1)
	
if __name__ == "__main__":
	main()

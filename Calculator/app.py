#Created by Karen Evans and Ethan Winters
#February 5, 2021
#My Simple Python Calculator

from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide


def choose():
	while True:
		print("Welcome to my python calculator. What would you like to do? ")
		print("1. Addition")
		print("2. Subtraction")
		print("3. Multiplication")
		print("4. Division")


		thislist = []
		y = True

		while True:
			try:
				user_selection = int(input("My choice is: "))
				if user_selection > 0 and user_selection < 5:
					break
				else:
					print("Only integers between 1 and 4 are allowed. Try again")
			# CalculatorInputError
			except ValueError:
				print("Only integers between 1 and 4 are allowed. Try again")

		while True:
			n1 = input("Type the number and press enter: ")
			print("To calculate type '=': ")
			
			if n1 == "=":
				break
			else:
				n1 = int(n1)
				thislist.append(n1)
		
		if user_selection == 1:
			answer = add(thislist)
			print("answer: " + str(answer))
			

		elif user_selection == 2:
			answer = subtract(thislist)
			print("answer: " + str(answer))
			

		elif user_selection == 3:
			answer = multiply(thislist)
			print("answer: " + str(answer))
			

		elif user_selection == 4:
			for x in range(len(thislist) - 1):
				if thislist[x] == 0:
					print("cannot divide by zero")
					print("")
					choose()
			answer = divide(thislist)
			print("answer: " + str(answer))

		else:
			print("Invalid selection. please try again")

		print("")

choose()
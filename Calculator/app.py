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
		print("5. To exit")

		user_selection = int(input("My choice is: "))

		if user_selection == 1:
			n1 = input("enter your first number: ")
			n2 = input("enter your second number: ")
			answer = add(n1, n2)
			print("answer: " + str(answer))
			

		elif user_selection == 2:
			n1 = input("enter your first number: ")
			n2 = input("enter your second number: ")
			answer = subtract(n1, n2)
			print("answer: " + str(answer))
			

		elif user_selection == 3:
			n1 = input("enter your first number: ")
			n2 = input("enter your second number: ")
			answer = multiply(n1, n2)
			print("answer: " + str(answer))
			

		elif user_selection == 4:
			n1 = input("enter your first number: ")
			n2 = input("enter your second number: ")
			answer = divide(n1, n2)
			print("answer: " + str(answer))
			

		elif user_selection == 5:
			print("Goodbye")
			break

		else:
			print("Invalid selection. please try again")
		print("")

choose()
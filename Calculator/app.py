import addition.py
import division
import multiplication
import subtraction

def select_function():
	print("Welcome to my python calculator. Please select from the following: ")

	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")

	user_selection = 0


	if user_selection == 1:
		addition.add_two_numbers(n1, n2)

	elif user_selection == 2:
		subtraction.subtract_two_numbers(n1, n2)

	elif user_selection == 3:
		multiplication.multiply_two_numbers(n1, n2)

	elif user_selection == 4:
		division.divide_two_numbers(n1, n2)


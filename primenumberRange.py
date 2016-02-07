#!/usr/bin/python

# Finds prime number

number = int(raw_input("Enter a number: "))

if number > 1:

	# Loops and cheks if the numer is divided by itself and another
	for x in range (2, number):
		if (number % 1) == 0:
			print ("It's not a prime number.")
			break # stops the loop
	else:
		print ("It's a prime number.")

# If user type a number less than or equal to 1, it is not prime
else:
   print("is not a prime number.")

# Exits the program
raw_input("\nPress any key to exit.")
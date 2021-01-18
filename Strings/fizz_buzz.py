def fizz_buzz():
	for number in range(1, 101):
		if number % 3 == 0:
			print("Fizz" + " " + str(number))
		if number % 5 == 0:
			print("Buzz" + " " + str(number))
		if number % 3 == 0 and number % 5 == 0:
			print("FizzBuzz" + " " + str(number))
fizz_buzz()

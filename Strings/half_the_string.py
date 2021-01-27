def half_string(string):
	x = string.replace(" ", "")
	if len(x) % 2 == 0:
		print(string[:int(len(x)/2)])
	else:
		print("Invalid string!")

x = input("Enter a string: ")
half_string(x)

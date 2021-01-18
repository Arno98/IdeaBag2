def happy_number(x):
	str_x = str(x)
	int_x = []
	square_x = []
	
	for y in str_x:
		int_x.append(int(y))
	
	for i in int_x:
		square_x.append(i ** 2)
	
	sum_x = sum(square_x)
	
	if sum_x == 1:
		return True
	if sum_x == 4:
		return False
	else:
		return happy_number(sum_x)

def happy_numbers(x):
	numbers = []
	start = 1
	while len(numbers) != x:
		func = happy_number(start)
		if func == True:
			numbers.append(start)
			start += 1
		else:
			start += 1
	print(numbers)
		
happy_numbers(8)

def happy_numbers_2():
	numbers = list(range(1, 10))
	for x in numbers:
		func = happy_number(x)
		if func == True:
			print(x)
			
happy_numbers_2()

dictt = {'fff': 'foo', 'zzz': 'aaa'}

x = input("Enter zzz: ")

if x == dictt['zzz']:
	print(x)
else:
	print("NOT")

	
	
	

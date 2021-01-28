def next_pn(x):
	next_num = x+1
	while True:
		for y in range(2, next_num):
			if next_num % y == 0:
				next_num += 1
				break
		else:
			print(next_num)
			break
next_pn(90)

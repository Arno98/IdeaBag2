num_of_rows = int(input("Enter num of rows: "))

triangle = [[1], [1, 1]]

def sum_func(x):
	row = []
	row.append(1)

	step_1 = 0
	step_2 = 2

	while step_2 != len(x)+1:
		row.append(sum(x[step_1:step_2]))
		step_1 += 1
		step_2 += 1
			
		if step_2 == len(x)+1:
			row.append(1)
			triangle.append(row)
	

while len(triangle) != num_of_rows:	
	sum_func(triangle[-1])
	if len(triangle) == num_of_rows:
		for row in triangle:
			print(row)
	

def latin_sqrt(n, l):
	if len(l) != n**2:
		print("Error! It is not sqrt!")
	else:
		iter_num = 0
		x = n
		y = 0
		z = 0
		sum_sqrt = sum(l[y:x])
		while iter_num != n:
			row = l[y:x]
			col = l[z::n]
			if sum(row) == sum_sqrt and sum(col) == sum_sqrt:
				y += n
				x += n
				z += 1
				iter_num += 1
				if iter_num == n:
					print(sum_sqrt)
					print("True")
			else:
				print("False")
				break
		
latin_sqrt(5, [1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 4, 5, 1, 2, 3, 3, 4, 5, 1, 2, 2, 3, 4, 5, 1])

def factorial(x):
	fact = 1
	while x != 1:
		fact *= x
		x -= 1
	print(fact)
factorial(5)

def factorial_recursion(x):
	if x == 0:
		return 1
	return factorial_recursion(x - 1) * x

print(factorial_recursion(5))


s = []

a = ['1', '2', '3', '4', '0']
b = ['1', '8', '3', '7', '5']

for x in a:
	for y in b:
		if x == y:
			s.append(x)

print(s)


from random import randint
from time import sleep

def coin_flip(x):
	count = 0
	values = []
	while count != x:
		print("Flip...")
		sleep(1)
		flip = randint(0, 1)
		print(flip)
		values.append(flip)
		count += 1
		
	tails = values.count(1)
	heads = values.count(0)
	
	print("Tails: " + str(tails))
	print("Heads: " + str(heads))
	
coin_flip(5)

print(2**38)


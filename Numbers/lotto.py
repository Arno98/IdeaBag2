from random import randint

def lotto():
	comp_numbers = []
	user_numbers = []
	while len(user_numbers) != 6:
		inp = input('Enter six numbers in range 1-49 (ex: 1 2 3 4 5 6): ')
		inp = inp.split()
		if len(inp) != 6:
			print("You must enter six numbers!")
			continue
		else:
			for x in inp:
				if int(x) > 49:
					print("You must enter number in range 1-49!")
					break
			else:
				for x in inp:
					user_numbers.append(int(x))
					comp_numbers.append(randint(1, 50))
					
				if user_numbers == comp_numbers:
					print(100)
				elif user_numbers[:5] == comp_numbers[:5]:
					print(80)
				elif user_numbers[:4] == comp_numbers[:4]:
					print(60)
				elif user_numbers[:3] == comp_numbers[:3]:
					print(40)
				elif user_numbers[:2] == comp_numbers[:2]:
					print(20)
				else:
					print(0)
									
				print(comp_numbers)
				print(user_numbers)
lotto()
		
	
	

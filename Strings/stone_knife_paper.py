import random
def game():
	values = ['Stone', 'Knife', 'Paper']
	while True:
		inp = input("Enter a value: ").title()
		if inp not in values:
			continue
		else:
			comp_choice = random.choice(values)
			print(inp)
			print(comp_choice)
			
			if comp_choice == inp:
				print('A tie')
			else:
				if (inp == values[0] and comp_choice == values[1]) or (inp == values[1] and comp_choice == values[2]) or (inp == values[2] and comp_choice == values[0]):
					print('Player win!')
				else:
					print('Comp win!')
			continue
game()

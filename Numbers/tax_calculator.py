def cost_with_tax(x, y):
	formula = x * (y / 100)
	total_cost = x + formula
	print("Total cost: " + str(total_cost) + "$")


def tax_calculator():
	tax_dict = {"California": 13.3, "Oregon": 9.9, "Washington": 0, "Nevada": 0, "Idaho": 7.4, "Montana": 6.9,
	            "Utah": 5, "Arizona": 4.54, "Waioming": 0, "Colorado": 4.63, "New-Mexico": 4.9, "North Dakota": 2.9,
	            "South Dakota": 0, "Nebraska": 6.84, "Kanzas": 4.6, "Oklahoma": 5, "Texas": 0}
	 
	start = True           
	while start:
		
		try:
			enter_an_account = float(input("Enter a main account: "))
			enter_a_tax = str(input("Where are you from: "))
			
		except ValueError:
			print("Please, enter a corect value. Try again")
			
		else:	
			for city, value in tax_dict.items():
				if enter_a_tax == city:
					cost_with_tax(enter_an_account, value)
					exit_or_no = str(input("Do you want repeat the process ? (enter 'y' for 'yes' or 'n' for 'no':) "))
					if exit_or_no == "y":
						continue
					elif exit_or_no == "n":
						start = False
						
			else:
				print("Please, enter a corect value (name of your state). Try again")
			
tax_calculator()

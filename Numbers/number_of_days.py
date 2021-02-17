def range_years(r):
	sum_days = 0
	for y in r:
		if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
			sum_days += 365
		else:
			sum_days += 366
	return sum_days

def number_of_days():
	date1 = input("Enter a first date (dd/mm/yyyy): ")
	date2 = input("Enter a second date (dd/mm/yyyy): ")
	
	num_of_days = 0
	
	if int(date1[6:]) == int(date2[6:]):
		None
	else:
		if int(date1[6:]) < int(date2[6:]):
			num_of_days += range_years(range(int(date1[6:]), int(date2[6:])))
		else:
			num_of_days += range_years(range(int(date2[6:]), int(date1[6:])))
		
	if int(date1[3:5]) == int(date2[3:5]):
		None
	else:
		if int(date1[3:5]) > int(date2[3:5]):
			num_of_days += (int(date1[3:5]) - int(date2[3:5])) * 30
		else:
			num_of_days += (int(date2[3:5]) - int(date1[3:5])) * 30
				
	if int(date1[:2]) == int(date2[:2]):
		None
	else:
		if int(date1[:2]) > int(date2[:2]):
			num_of_days += int(date1[:2]) - int(date2[:2])
		else:
			num_of_days += int(date2[:2]) - int(date1[:2])
			
	print(num_of_days)
		
number_of_days()
	

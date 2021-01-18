def username_generator():
	full_name = str(input("Enter a full name: "))
	
	list_full_name = full_name.split()
	
	len_first_name = len(list_full_name[0])
	len_second_name = len(list_full_name[1])
	
	x = 1
	y = 2
	
	while x != len_first_name and y != len_second_name:
		print(list_full_name[0][:x].lower() + list_full_name[1][:y].lower())
		y += 1
		if y == len_second_name:
			x += 1
			y = 1
			
username_generator()

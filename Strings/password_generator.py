from random import randint

def password_generator(length):
	x1 = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
	x2 = '1234567890'
	x3 = '!@#$%^&_/*-+?><:;'
	
	password = ''
	while len(password) != length:
		ran = randint(1, 3)
		if ran == 1:
			ran_x1 = randint(0, len(x1))
			password += x1[ran_x1-1]
		if ran == 2:
			ran_x2 = randint(0, len(x2))
			password += x2[ran_x2-1]
		if ran == 3:
			ran_x3 = randint(0, len(x3))
			password += x3[ran_x3-1]
	print(password)
	
password_generator(24)

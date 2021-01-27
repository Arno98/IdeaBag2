def oodle(word):
	voowels = 'eyuioa'
	word2 = ''
	for x in word:
		if x not in voowels:
			word2 += x
	print('oodle'.join(word2))
oodle("dog and cat")

def compute_grade():
	while True:
		score = input('Enter score from 0.0 to 1.0: ')
		try:
			if len(score) == 0:
				print ('enter a value')
			else:	
				num_score = float(score)
				if num_score <= 1.0:
					if num_score >= 0.9:
						print ('Grade A')
					elif num_score >= 0.8:
						print ('Grade B')
					elif num_score >= 0.7:
						print ('Grade C')
					elif num_score >= 0.6:
						print ('Grade D')
					elif num_score < 0.6:
						print ('Grade F')
					break
				else:
					print('enter correct range 0.0 t0 1.0')
		except:
			print ('enter poper data type float')

# compute_grade()

def richard():
	direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
	verbs=["go", "stop", "kill", "eat"]
	stop_words=["the", "in", "of", "from", "at", "it"]
	nouns=["door", "bear", "princess", "cabinet"]
	numbers=["0","1","2","3","4","5","6","7","8","9"]

	words = raw_input("Insert: ")

	splited = words.lower().split()
	# splited = set(splited)
	splited = sorted(set(splited))

	print splited

	sentence = []
	wrong = []

	for word in splited:
		if word in direction:
			sentence.append(('direction', word))
		elif word in verbs:
			sentence.append(('verbs', word))
		elif word in stop_words:
			sentence.append(('stop_words', word))
		elif word in nouns:
			sentence.append(('nouns', word))
		elif word in numbers:
			sentence.append(('numbers', word))
		else:
			wrong.append(word)
	print "\n", sentence, " are the word/s which are in the program"
	print "\n", wrong, " are the word/s which are not in the program\n"

	first_word=""
	second_word=""
	third_word=""
	fourth_word=""

	for word in sentence:
		if word[0]=="stop_words":
			first_word=word[1]
		if word[0]=="nouns":
			second_word=word[1]
		if word[0]=="verbs":
			third_word=word[1]
		if word[0]=="direction":
			fourth_word=word[1]

	print first_word,second_word,third_word,fourth_word
	print sentence

# richard()
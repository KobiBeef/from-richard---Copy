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

compute_grade()
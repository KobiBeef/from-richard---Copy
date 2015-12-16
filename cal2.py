import random
# 4 item filter design
# scan_input(x)
# scan_operation(scan_input(x))
# scan_total_item(scan_input(x))
# scan_user_ans(scan_input(x))
# scan_ch(scan_input(x))


def scan_input(para1):
	user_input = para1.split()
	# try:
	# if (len(user_input) == 0) or (len(user_input) > 1):
	# 	pass
	if len(user_input) == 0:
		print "enter a value"
	elif len(user_input) > 1: 
		print "enter only a single value"
	else:
		user_input = int(user_input[0])
		return user_input 
			# if user_input <= 0:
			# 	print "enter numbers greater than 0"
			# elif user_input > 4:
			# 	print "enter only 1 -4"
			# else:
			# 	return False
	# except :
	# 	print "enter integers only"
		

class MathDrill():
	def __init__(self):
		self.no_item = ""
		self.operator = ""
	
	def isCheck(self, num_1, num_2, ans, opt):
		if opt==1: 
			if (num_1 + num_2) == ans:
				return True
		elif opt==2: 
			if((n1-n2)==ans):
				return True
		elif opt==3: 
			if((n1*n2)==ans):
				return True
		elif opt==4: 
			if((n1/n2)==ans):
				return True
		else:
			return False

	# which is a better design?
		# - integerating the isCheck in the doFunctions? OR
		# - separating the isCheck from the doFunctions?

	def isPassed(self, score):
		if score >= self.no_item/2:
			print "You Passed!"
		else:
			print "You Failed!"

	# reuse of the opt==1 variable from main3.py
	def doAddtion(self, opt):
		score = 0
		# x=1
		item_num = 1
		# item_num starts with the value of 1
		while item_num <= self.no_item:
			num_1 = random.randint(1,10)
			num_2 = random.randint(1,10)
			ans = num_1 + num_2
			print "%d. %d + %d = ?" % (item_num, num_1 ,num_2)
			#########################################
			# filter user_ans_input to integers only#
			# must not accept null/empty input      #
			#########################################
			while True:
				user_ans_input = raw_input("ur answer is > ")
				try:
					if len(user_ans_input) == 0:
						print "enter a value"
					else:
						user_ans_input_to_int = int(user_ans_input)
						break
				except:
					print "enter integers only"
			# if (user_ans_input == ans) == self.isCheck(num_1, num_2, ans ,1):
			if self.isCheck(num_1, num_2, ans, opt=opt):
			# this checks if the computer answer is correct
				if ans == user_ans_input_to_int:
				# this checks if user answer is correct
					score+=1
					print "That's Correct!"
				else:
					print "Sorry, That's Wrong!"
			item_num+=1
			# while exit if item_num > self.no_item
		# use a isPassed function here
		self.isPassed(score)

		
	def doSubtraction(self):
		score=0
		x=1
		while x<=self.numbers:
			n1=random.randint(1,10)
			n2=random.randint(1,10)
			ans=n1+n2
			print "%d. %d - %d = ?" % (x,n1,n2)
			if(self.isCheck(n1,n2,ans,2)):
				score+=1
				print "That's Correct!"
			else:
				print "Sorry, That's Wrong!"
			if(score>=(self.numbers/2)):
				print "You Passed!"
			else:
				print "You Failed!"
			x+=1
		
	def doMultiplication(self):
		score=0
		x=1
		while x<=self.numbers:
			n1=random.randint(1,10)
			n2=random.randint(1,10)
			ans=n1+n2
			print "%d. %d * %d = ?" % (x,n1,n2)
			if(self.isCheck(n1,n2,ans,3)):
				score+=1
				print "That's Correct!"
			else:
				print "Sorry, That's Wrong!"
			if(score>=(self.numbers/2)):
				print "You Passed!"
			else:
				print "You Failed!"
			x+=1
		
	def doDivision(self):
		score=0
		x=1
		while x<=self.numbers:
			n1=random.randint(1,10)
			n2=random.randint(1,10)
			ans=n1+n2
			print "%d. %d / %d = ?" % (x,n1,n2)
			if(self.isCheck(n1,n2,ans,4)):
				score+=1
				print "That's Correct!"
			else:
				print "Sorry, That's Wrong!"
			if(score>=(self.numbers/2)):
				print "You Passed!"
			else:
				print "You Failed!"
			x+=1
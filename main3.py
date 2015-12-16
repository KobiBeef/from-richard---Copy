from cal2 import MathDrill, scan_input
rich=MathDrill()
name=raw_input("Please Enter Your Name: ")
print "\nHi, %s\n\nWelcome To The Math Drill and Practice Program" % name

ch=0	
while ch!=1:
	while True:
		opt = raw_input("\nPlease Select Operation:\nAddition:\t1\nSubtraction:\t2\nMultiplication:\t3\nDivision:\t4\n")
		try:
			opt = scan_input(opt)
			if opt <= 0:
				print "enter positive numbers only"
			elif opt > 4:
				print "enter values 1 - 4 only"
			else:
				break
		except:
			print "enter integers only"
		# try:
		# 	if len(opt) == 0:
		# 		print "enter a value"
		# 	elif len(opt) > 1:
		# 		print "enter value 1, 2, 3, and 4 only"
		# 	else:
		# 		opt = int(opt)
		# 		if opt <= 0:
		# 			print "input positive numbers only"
		# 		elif opt > 4:
		# 			print "enter value 1, 2, 3, and 4 only"
		# 		else:
		# 			break
		# except:
		# 	print "enter integer only"
	# opt=int(raw_input("\nPlease Select Operation:\nAddition:\t1\nSubtraction:\t2\nMultiplication:\t3\nDivision:\t4\n"))
	# put a input guardian for variable opt: should not accept string/s and interger below 1 and above 4

	while True:
		total_item=raw_input("\nHow Many Items Would You Like To Answer? ")
		total_item = total_item.split()
		try:
			if len(total_item) == 0:
				print "enter how many items would you like to answer"
			elif len(total_item) > 1:
				print "enter only one value of items you would like to answer"
			else:
				total_item = int(total_item[0])
				break
		except :
			print "enter integers only or any value above zero"
	# total_item=int(raw_input("\nHow Many Items Would You Like To Answer? "))
	# put a input guardian for the variable totalItem: should not accept string/s input

	# would try to put the user_input() filter to one function then call
	# def filter_user_input
	#########################################
	# similarities in the scan_input_filter #
	#########################################
	# 1. gets a user_input
	# 2. split() the user_input to check if data entry is more than 1 and is less or equal to 0
	# 3. other options would depend on the input needed

	rich.no_item=total_item
	if opt==1: 
		rich.doAddtion(opt)
	if opt==2: 
		rich.doSubtraction()
	if opt==3: 
		rich.doMultiplication()
	if opt==4: 
		rich.doDivision()
	ch=int(raw_input("\nWould You Like To Try Another? 1 for No 0 for Yes\n"))
	# put an input guardian for variable ch: should not accept string/s and numbers below 0 and above 1
	# ch variablae input exits or continous the while loop
else:
	print "\nThank You %s For Using The Program!\n\nSee You On The Next Math Drill...\n\n\nProgrammed by II-3\nGroup 6:\nMary Rose L. Moises\nMikarla Lyn M. Molina\nRichard A. Ongpin\nJane A. Paculan\nMary Gayle L. Padrinao" % name
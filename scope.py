# num = 8
# def double (num):
# 	doubled = num * 2
# 	return doubled

# print double(num)

# score = 0
# def increase_score(points):
# 	new_score = score + points
# 	return new_score

# print score
# print increase_score(10)

# score = 0

# def increase_score(points):
# 	new_score= score + points
# 	return new_score

# print score
# score = increase_score(10)
# print score

# global_variable = 13.4

# def function_one():
# 	do_something


# def function_two():
# 	do_something

# ()
# def main():
# 	if (condition == true):
# 		function_one
# 	else:
# 		function_two

# if __name__=='__main__':
# 	main

def calculate_tip(bill_amount, tip_percentage):
	return bill_amount * tip_percentage *.01

def total_bill(tip_amount, bill_amount):
	return tip_amount + bill_amount

def split_bill(total_bill, num_people):
	return total_bill / num_people

def main():

	bill_amount = float(raw_input("Please enter bill amount: "))
	tip_amount = float(raw_input("Please enter tip percentage: "))
	answer = raw_input("Enter 1 to calculute tip or enter 2 to split bill: ")

	
	if(answer == "1"):
		tip = calculate_tip(bill_amount, tip_amount)
		print "The tip is: $", tip, "  The total bill with tip is $", bill_amount + tip
	answer2 = raw_input("Would you like to split bill? ")
	if (str.lower(answer2) == "yes"):
		bill= tip + bill_amount
		num_people = float(raw_input("How many ways? "))
		split = split_bill(bill, num_people)
		print "Each person owes: $", split
	if(answer =="2"):
		num_people= float(raw_input("How many ways? "))
		split= split_bill(bill_amount,num_people)
		print "Each person owes: $", split
	
	
	else:
		print "Have a good day!"
	

if __name__ == '__main__':
		main()





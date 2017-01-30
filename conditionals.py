# age = int(raw_input("How old are you? "))
# if age > 21:
# 	print "Yay! I can vote and go to a bar"
# else:
# 	if age > 18:
# 		print "I can only vote!"
# 	else:
# 		print "Too young for everything :/"

# num = int(raw_input("Enter a number: "))
# if(num % 2 == 0):
# 	print "Even"
# else:
# 	print "Odd"

num1 = int(raw_input("Enter a number: "))
num2= int(raw_input("Enter another number: "))
if (num1 % 2 ==0 and num2 % 2 == 0):
	print "Both numbers are even!"
else:
	if (num1 % 2 != 0 and num2 % 2 ==0):
		print num1, "is odd and", num2, "is even!"
	elif (num1 % 2 == 0 and num2 % 2 != 0):
		print num1, "is even and", num2, "is odd!"
	else:
		print "Both numbers are oddballs!"

print "poop github"


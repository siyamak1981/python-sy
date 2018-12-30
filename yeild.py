# A simple generator function
def mygen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
# out:
# >> from test import mygen
# >>> a = mygen()
# >>> a
# <generator object mygen at 0x000001DE37FA7408>
# >>> next(a)
# This is printed second
# 2
# >>> next(a)
# This is printed at last
# 3
# >>> next(a)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# #############################################
# حالا بدون دستور شل اینجوری میتونیم اقدام کنیم که تو این صفحه ویژوال اجرا بگیرم
for item in mygen():
    print(item) 
# out:
# This is printed first
# 1
# This is printed second
# 2
# This is printed at last
# 3
# #######################################
# A Simple Python program to demonstrate working 
# of yield 

# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
	yield 1
	yield 2
	yield 3

# Driver code to check above generator function 
for value in simpleGeneratorFun(): 
	print(value) 
# @#######################################
# A Python program to generate squares from 1 
# to 100 using yield and therefore generator 

# An infinite generator function that prints 
# next square number. It starts with 1 
def nextSquare(): 
	i = 1; 

	# An Infinite loop to generate squares 
	while True: 
		yield i*i				 
		i += 1 # Next execution resumes 
				# from this point	 

# Driver code to test above generator 
# function 
for num in nextSquare(): 
	if num > 100: 
		break	
	print(num) 

# out:
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
# ##################################
# اگر بجای یلد ریترن بزاریم این ارور و میده
# Traceback (most recent call last):
#   File "1.py", line 12, in <module>
    # for num in nextSquare():
# TypeError: 'int' object is not iterable
# #########################################
def print_even(test_list) : 
	for i in test_list: 
		if i % 2 == 0: 
			yield i 

# initializing list 
test_list = [1, 4, 5, 6, 7] 

# printing initial list 
print ("The original list is : " + str(test_list)) 

# printing even numbers 
print ("The even numbers in list are : ", end = " ") 
for j in print_even(test_list): 
	print (j, end = " ")
# out:
# The original list is : [1, 4, 5, 6, 7]
# The even numbers in list are :  4 6
# ###################################
# Python3 code to demonstrate yield keyword 

# Checking number of occurrence of 
# geeks in string 

# generator to print even numbers 
def print_even(test_string) : 
	for i in test_string: 
		if i == "geeks": 
			yield i 

# initializing string 
test_string = " The are many geeks around you, \
			geeks are known for teaching other geeks" 

# printing even numbers using yield 
count = 0
print ("The number of geeks in string is : ", end = "" ) 
test_string = test_string.split() 

for j in print_even(test_string): 
	count = count + 1

print (count) 

# out:
# The number of geeks in string is : 3
# ریترن بزاریم باز هم ارور بالا رو میده
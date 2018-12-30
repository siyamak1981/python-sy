# Python code to illustrate 
# reduce() with lambda() 
# to get sum of a list 
from functools import reduce
li = [5, 8, 10, 20, 50, 100] 
sum = reduce((lambda x, y: x + y), li) 
print (sum) 
# 193
# @###################################3
# Python program to Find the Number 
# Occurring Odd Number of Times 
# using Lambda expression and reduce function 

from functools import reduce

def oddTimes(input): 
	# write lambda expression and apply 
	# reduce function over input list 
	# until single value is left 
	# expression reduces value of a ^ b into single value 
	# a starts from 0 and b from 1 
	# ((((((1 ^ 2)^3)^2)^3)^1)^3) 
	print (reduce(lambda a, b: a ^ b, input)) 

# Driver program 
if __name__ == "__main__": 
	input = [1, 2, 3, 2, 3, 1, 3] 
	oddTimes(input) 

# ========>>>out : 3

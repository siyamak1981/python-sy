# Double all numbers using map and lambda 

numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, numbers) 
print(list(result)) 
# [2, 4, 6, 8]
# ##############################################
# Add two lists using map and lambda 

numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 

result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) 
# [5, 7, 9]
# ##############################################
# >>> sum = lambda x, y : x + y
# >>> sum(3,4)
# 7
# >>> 
# =====>>>>
# >>> def sum(x,y):
# ...     return x + y
# ... 
# >>> sum(3,4)
# 7
# >>>
# ##################################################
# Python code to illustrate cube of a number 
# showing difference between def() and lambda(). 
def cube(y): 
	return y*y*y; 

g = lambda x: x*x*x 
print(g(7)) 

print(cube(5)) 
# 343
# 125
# #####################33



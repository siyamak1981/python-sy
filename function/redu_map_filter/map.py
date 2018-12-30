def myfunc(a):
    return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)
# <map object at 0x0000019E98E8DC50>
#convert the map into a list, for readability:
print(list(x))
# [5, 6, 6]
# ########################################
def func(a):
     
   return a
#    return a
    

x = map(func,("siyamak","diyana","sami"))

print(list(x))

# ['siyamak', 'diyana', 'sami']
# ##################################3333
def myfunc(a, b):
      return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(x)
# <map object at 0x0000019E98E8DCF8>
#convert the map into a list, for readability:
print(list(x))
# ['appleorange', 'bananalemon', 'cherrypineapple']
######################################################


# Python program to demonstrate working 
# of map. 

# Return double of n 
def addition(n): 
	return n + n 

# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 
# [2, 4, 6, 8]
# #############################################3333
# List of strings 
l = ['sat', 'bat', 'cat', 'mat'] 

# map() can listify the list of strings individually 
test = list(map(list, l)) 
print(test) 
# [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]
# ####################################################
# >>> def fahrenheit(T):
# ...     return ((float(9)/5)*T + 32)
# ... 
# >>> def celsius(T):
# ...     return (float(5)/9)*(T-32)
# ... 
# >>> temperatures = (36.5, 37, 37.5, 38, 39)
# >>> F = map(fahrenheit, temperatures)
# >>> C = map(celsius, F)
# >>>
# >>> temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
# >>> temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))
# >>> print(temperatures_in_Fahrenheit)
# [97.7, 98.60000000000001, 99.5, 100.4, 102.2]
# >>> print(temperatures_in_Celsius)
# [36.5, 37.00000000000001, 37.5, 38.00000000000001, 39.0]
# ##########################################################3
x = (7, 2)
g = map(lambda x: x * x * x, x) 
print(list(g))
# out [343, 8]

# ##################3




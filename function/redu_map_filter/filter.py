# Python code to illustrate 
# filter() with lambda() 
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list) 
# [5, 7, 97, 77, 23, 73, 61]
# #######################################
# Python Program to find numbers divisible 
# by thirteen from a list using anonymous 
# function 

# Take a list of numbers. 
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ] 

# use anonymous function to filter and comparing 
# if divisible or not 
result = list(filter(lambda x: (x % 13 == 0), my_list)) 

# printing the result 
print(result) 
# [65, 39, 221]
# ############################################
numbers = (1, 2, 3, 4) 
result = filter(lambda x: x + x, numbers) 
print(list(result))
# ============>>این + در اینجا ج نمی ده بهتر است از مپ استفاده بشه
# [1, 2, 3, 4]
# ############################################
my_list = ["geeks", "geeg", "keek", "practice", "aa"] 
  
# use anonymous function to filter palindromes. 
# Please refer below article for details of reversed 
# https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/ 
result = list(filter(lambda x: (x == "".join(reversed(x))), my_list))  
  
# printing the result 
print(result) 
# =====>>out:['geeg', 'keek', 'aa']
# ################################################
# Python Program to find all anagrams of str in 
# a list of strings. 
from collections import Counter 

my_list = ["geeks", "geeg", "keegs", "practice", "aa"] 
str = "eegsk"

# use anonymous function to filter anagrams of x. 
# Please refer below article for details of reversed 
# https://www.geeksforgeeks.org/anagram-checking-python-collections-counter/ 
result = list(filter(lambda x: (Counter(str) == Counter(x)), my_list)) 

# printing the result 
print(result) 
# =====>>out : ['geeks', 'keegs']
# ########################################################
ages = [5, 12, 17, 18, 24, 32]
res = filter(lambda x : x >= 18 , ages)
for x in res:
    print(x)
# =====>>out:
# 18
# 24
# 32
# ##############################################





['geeks', 'keegs']
18
24
32
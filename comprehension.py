nums = range(1,10)
have = []
for num in nums:
    have.append(num/2)
    print(have)  
# out
# [0.5]
# [0.5, 1.0]
# [0.5, 1.0, 1.5]
# [0.5, 1.0, 1.5, 2.0]
# [0.5, 1.0, 1.5, 2.0, 2.5]
# [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
# [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
# [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
# [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
# ########################################################
# >>> nums = range(1, 10)
# >>> have = []
# >>> for num in nums:
# ...     have.append(num)
# ...
# >>> have
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # ################################################
# >>> nums = range(1, 10)
# >>> have = []
# >>> have(num/2 for num in nums)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'list' object is not callable
# >>> have[num/2 for num in nums]
#   File "<stdin>", line 1
#     have[num/2 for num in nums]
#                  ^
# SyntaxError: invalid syntax
# >>> have=[num/2 for num in nums]
# >>> have
# [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
# >>>
# ##############################################
print([num/2 for num in range(1,10) if num %3 == 0])
# out
# [1.5, 3.0, 4.5]
# # #############################################
row = range(4)
col = range(10)
g=[(x,y) for x in col for y in row ]
print (g)
# ##############################################3
# out

# [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3), (5, 0), (5, 1), (5, 2), (5, 3), (6, 0), (6, 1), (6, 2), (6, 3), (7, 0), (7, 1), (7, 2), (7, 3), (8, 0), (8, 1), (8, 2), (8, 3), (9, 0), (9, 1), (9, 2), (9, 3)]
# #################################################
d = {number: letter for letter ,number in zip("lkdjgljdlgg",range(1,10))}
print(d)
# out
# {1: 'l', 2: 'k', 3: 'd', 4: 'j', 5: 'g', 6: 'l', 7: 'j', 8: 'd', 9: 'l'}
# ###########################################################

total=range(1,100)
fizzbuzz= {
    'fizz' :[n for n in total if n %3 ==0], 
    'buzz ':[n for n in total if n %2 == 0]
}

print(fizzbuzz)
# out
# {'fizz': [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99],
#  'buzz ': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66,
# 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]}
# #######################################################
x ={ round(x/y) for y in range(1,20) for x in range(1,9)}
print(x)
# out
# {0, 1, 2, 3, 4, 5, 6, 7, 8}
# ####################################3
h = [round(x/y) for y in range(1,20) for x in range(1,9)]
print(h)
# out
# [1, 2, 3, 4, 5, 6, 7, 8, 0, 1, 2, 2, 2, 3, 4, 4, 0, 1, 1, 1, 2, 2, 2, 3, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 1, 1, 1, 1, 1, 2, 0, 0, 0, 1, 1, 1,
# 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# #################################################################

total=range(1,100)
fizzbuzz= {
    'fizz' :[n for n in total if n %3 ==0], 
    'buzz ':[n for n in total if n %2 == 0]
}
# fizzbuzz = {key : set(value) for key,value in fizzbuzz.items()}
fizzbuzz['fizzbuzz'] = {n for n in fizzbuzz['fizz'].intersection(fizzbuzz['buzz']) }
print(fizzbuzz)


# ##========> to comprehensions cant to use (tuples) and (strings) bec thay are immutable
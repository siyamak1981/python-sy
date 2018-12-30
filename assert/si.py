print(1)
assert 1 + 1 == 2
print(2)
assert 2 + 3 == 8
print(3)


# $ python si.py
# 1
# 2
# Traceback (most recent call last):
#   File "si.py", line 51, in <module>
#     assert 2 + 3 == 8
# AssertionError
# #########################################
def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0),"Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(263))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))  
# out:
# 14.0
# 451
# Traceback (most recent call last):
#   File "si.py", line 22, in <module>
#     print (KelvinToFahrenheit(-5))
#   File "si.py", line 17, in KelvinToFahrenheit
#     assert (Temperature >= 0),"Colder than absolute zero!"
# AssertionError: Colder than absolute zero! 
# ###############################################

# import unittest
class  N :
    
    def __init__(self,a, b):
        self.a = a
        self.b = b
    def  add(self):
        assert(self.a > self.b)
        return '{} > {}'.format(self.a,self.b)
        

# p = N()
# print(p.add())



# >>> p = N(5, 4)
# >>> p
# <si.N object at 0x000001F262F12CF8>
# >>> p.add
# <bound method N.add of <si.N object at 0x000001F262F12CF8>>
# >>> p.add()
# '5 > 4'

# ###############################3
# >>> p = N(5, 7)5
# >>> p
# <si.N object at 0x000001C38E0F2940>
# >>> p.add()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "D:\website\python37\python.sa\siyamak\si.py", line 21, in add
#     assert(self.a > self.b)
# AssertionError

# #######################################

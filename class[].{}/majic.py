class Example:
  
    def __init__ (self, a , b):
        self.a = a
        self.b = b
  
    def __add__(self,other):
        return Example(self.a + other.a, self.b + other.b)

    def __str__(self):
        return "({0},{1})".format(self.a,self.b)

obj1 = Example(1,2)
obj2 = Example(3,4)
obj3 = Example(1.2,2.2)
print (obj1 + obj2)
    #  (4,6)
print (obj1 + obj3)
# (2.2,4.2)
# #################################################
class Example:
    def __init__(self,a,b):
        self.a = a
        self.b = b
 
    def __str__(self):
        return "({0},{1})".format(self.a,self.b)
 
    def __iadd__(self,other):
        self.a += other.a
        self.b += other.b
        return Example(self.a,self.b)

obj1 = Example(1,2)
obj2 = Example(2,3)
obj2 += obj1
print (obj2)
# (3,5)
# ######################################
class Example:
    def __init__(self,a):
        self.a = a
 
    def __gt__(self,other):
        return self.a > other.a

obj1 = Example(1)
obj2 = Example(2)
print (obj2 > obj1)
# True
# #######################################
class Numstring:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value) 

    def __float__(self):
        return float(self.value)
        # immutable add
    def __iadd__(self,other):
        self.value = self + other
        return self.value
   
    def __add__(self,other):
        if '.' in self.value:
            return float(self)+ other
        return int(self) + other

        # reverse add for example 5 + five
    def __radd__(self, other):
        return self + other

    
a = Numstring(5)
print (a + 5)
print (a + 5.5555)
print ( 4.55+ a)  



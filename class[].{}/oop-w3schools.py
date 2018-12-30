class MyClass:
    x = 5
p = MyClass()


print(MyClass)
print(p.x)

# out:
# <class '__main__.MyClass'>
# 5
# ##########################################
class C:
    i = 5

z = C()
z.i = 599
print(z.i)
print(C.i)


# out:
# 599
# 5
# ###########################################

class C:
    def p(self):
        print(self.name)


x = C()
x.name = "siyamak"
d = C()
d.age=555885
print(x.p())
print(d.age)
# out:
# siyamak
# None
# 555885 پایتون با اشیا کار میکنه نه با کلاسها
# #####################################
# $ python
# Python 3.7.1rc2 (v3.7.1rc2:6c06ef7dc3, Oct 13 2018, 15:44:37) [MSC v.1914 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from tet import C
# >>> x.C(5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'x' is not defined
# >>> x = C()
# >>> x
# <tet.C object at 0x00000292D82129B0>
# >>> x.p
# <bound method C.p of <tet.C object at 0x00000292D82129B0>>
# >>> x.p()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "D:\website\python37\python.sa\siyamak\tet.py", line 4, in p
#     print(self.name)
# AttributeError: 'C' object has no attribute 'name'
# #################################################
# out:
# >>> from tet import C
# >>> x = C()
# >>> C.p
# <function C.p at 0x000001500BB689D8>
# >>> x.name = "siyamak"
# >>> x
# <tet.C object at 0x000001500BD02940>
# >>> x.name
# 'siyamak'
# >>> x.p
# <bound method C.p of <tet.C object at 0x000001500BD02940>>
# >>> x.p()
# siyamak
# >>> C.p()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: p() missing 1 required positional argument: 'self'
# >>> C.name
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: type object 'C' has no attribute 'name'


#  r = C()
# >>> r.name
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'C' object has no attribute 'name'
# name به اشیا اضافه شدخ نه به کلاس


# >>> from tet import C
# >>> x = C()
# >>> x.p = 123
# >>> x.name
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'C' object has no attribute 'name'
# >>> x.p() = 88888
#   File "<stdin>", line 1
# SyntaxError: can't assign to function call
# ######################################3
# ############################

class New():
    
    def __init__(self):
        self.name = "siyamak"
     

p=New()
print(p.name)

# out:
# siyamak
# ####################################
class C:
    pass

def p(self,args):
    self.name = args
    return self.name
f = C()
x = C()
C.method = p
x.method("j")
# x.name = 888
print(f.name)
print(x.name)
print(x.method)
print(x.method(65))
# out:
# AttributeError: 'C' object has no attribute 'name'
# j
# <bound method p of <__main__.C object at 0x000001DD5E69C240>>
# 66
# ##########################################

name = "siyamak"

class C :
    name = "diyana"
    def __init__(self, name):
        self.name = "sami"
    def p(self):
        name = "saeed"
        return name
        # print(self.name)
        # print(C.name)

v=C("maman")
print(v.name)
print(v.p())
print(name)
print(C.name)

# out:
# sami
# saeed
# siyamak
# diyana

# ########################################3

class New:
    def __init__(self):
        name = []
        # self.name = []فرقی نداره سلف باشه یا نه
p=New()
p.name = "lkd",1,"python", 555
print(p.name)
# out:
# ('lkd', 1, 'python', 555)
# ##################################

class New():
    job="best programing in python"
    def __init__(self):
        name = "author"
        print(name)
        
p=New()
p.name = "siyamak"
print(p.name)
print(p.job)

# out:
# author
# siyamak
# best programing in python
# ################################
class N :
        job = "i am best developer"
        def __init__(self):
               self.a = "skm"


        def add(self):
                return self.a
s = N()
          
print(s.add())
# out:
# skm
# #########################################

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("siyamak", 36)

print(p1.name)
print(p1.age)
# ########################################
class Person:
    def __init__(self, name, age):
        self.fg = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.fg)

p1 = Person("John", 36)
p1.myfunc()
# #############################################
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abcd):
        print("Hello my name is " + abcd.name)

p1 = Person("sajad", 36)
p1.myfunc()
# out:
# Hello my name is sajad
# ##############################################
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("saeden", 45)

p1.age = 40

print(p1.age)
# out:
# 40
# #########################################
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age

print(p1.age)
# ##############################################

###===>> variable private<<=====####
class D():
    _age = None
    __mof = None
    def __init__(self):
        self.name = 'doberman'
        D._age = 35
        D.__mofF= "kdvj"


    def _print(self):
        print(self.name, D._age,D.__mofF )

# out:
# >>> x = D()
# >>> x._print
# <bound method D._print of <tet.D object at 0x00000166024E2940>>
# >>> x._print()
# doberman 35 kdvj


# #############################################
class New():
    job="best programing in python"
    
    def print_it():
        print("blue_python")
    def __init__(self):
        name = "author"
        city = "shomal"
        self.ilts = 8
        print(name,city.upper())
        self.language = "english"
    def getlanguage(self):
        return self.language


New.print_it()       
p=New()
p.name = "siyamak"

print(p.name)
print(p.job)
print("siyamak has ilts {}".format(p.ilts))
print(p.getlanguage())

# out:
# blue_python
# author SHOMAL
# siyamak
# best programing in python
# siyamak has ilts 8
# english
# ######################################################

class Z(object):
    name = ['dober','shiyanlo']
    age = 5
    def Print(self):
        print('name:',self.name)
        print('age:',self.age)

class X(object):
    def x(self) :
        print('X')



class Dog(Z,X):
    breed=""
    def Print(self):
        print('breed',self.breed)
        super().Print()

# out:
# >>> from tet import Dog
# >>> o = Dog()
# >>> o.Print()
# breed
# >>> o.name
# ['dober', 'shiyanlo']
# >>> o.age
# 5
# >>> o.name = "gorgi"
# >>> o.name
# 'gorgi'
# >>> o.x
# <bound method X.x of <tet.Dog object at 0x000001CC0BD129B0>>
# >>> o.x()
# X
# ##############################################################
# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog() class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog() class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)
print(jim.description())

# Child classes have specific attributes
# and behaviors as well
print(jim.run("slowly"))

# Is jim an instance of Dog()?
print(isinstance(jim, Dog))

# Is julie an instance of Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

# Is johnny walker an instance of Bulldog()
johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))

# Is julie and instance of jim?
print(isinstance(julie, jim))
# #############################################

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00



# test code
print(car1.description())
# #############################################################
class Lang:
    ilts = True

    def __init__(self,name,lang):
       self.name = name
       self.lang = lang

    def degree(self):
        print("congratulate {} u got ur {} ilts".format(self.name, self.lang))     

tafel = Lang("siyamak",7)
tafel.degree()

print(tafel.name)
print(tafel.lang)

# ##################################3333
class PostStatus:
    """Check Published or Draft Status of a post
    
    Arguments:
        is_charfield {[bool]} -- check for charfield models or positiveintegerfield
    """
    def __init__(self, is_charfield = True):
               
        if is_charfield:
            self.DRAFT = 'd'
            self.PUBLISHED = 'p'
        else:
            self.DRAFT = 0
            self.PUBLISHED = 1        

    def is_published(self, value):
        """[summary]
        Arguments:
            Postable {[str, int]} -- [description]
        Returns:
            [type] -- [description]
        """
        return True if value == self.PUBLISHED else False
    
    def is_draft(self, value):
        return True if value == self.DRAFT else False
    
    def get_draft(self):
        return self.DRAFT
    
    def get_publish(self):
        return self.PUBLISHED
    
    def get_status(self):
        status = (
            (self.DRAFT, 'Draft'),
            (self.PUBLISHED, 'Published'),
        )

        return status
# #################################################################

import random 
class Choices():
    draft = ''
    published = 1
    def __init__(self):
        self.draft = "drfat"
        self.published = "published"

    def getpublish(self):
        return self.published
      
    def getdraft(self):

        return self.draft

k = Choices()
print(random.randint(0,1))
# ###############################################

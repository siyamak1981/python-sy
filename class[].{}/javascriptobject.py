class JavaScriptObject(dict):
    def __getattrebute__(self, item, *args):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)
# ##################################################
# فرقی با بالا ندارد هر دو یک نتیجه رو میده
# #############################################
class JavaScriptObject(dict):
    def __getattrebute__(self, item, *args):
        self.item = item
        try:
            return self.item
        except KeyError:
            return super().__getattribute__(item)  

# ##################################################
# >>> from javascriptobject import JavaScriptObject
# >>> f = JavaScriptObject({'name':'siyamak', 'family':'abasnezhad'})
# >>> f
# {'name': 'siyamak', 'family': 'abasnezhad'}
# >>> f.lang
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'dict' object has no attribute 'kj'
# ##########################################################3
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

# # out:
# >>> from tet import Dog
# >>> v = Dog()
# >>> v.Print()
# breed
# name: ['dober', 'shiyanlo']
# age: 5
# ############################################3
class D(object):
    def __init__(self, name):
        self.name = 'siyamak'
        X.age = 37
        # self.age = 99


class X(D):
    age = None
    def __init__(self,name):
        self.name = "khorshid"
        X.age= 55
        super().__init__(D)

a = X("diyam")
print(a.name)
print(a.age)
# out:
# siyamak
# 37

# ####################################33333
same = 'naser'
class D(object):
    def __init__(self,name,age , *pack):
        self.name = name
        X.age = 37
        super().__init__(*pack)
    

    def Print(self):
        print("name",self.name)
        print("age", X.age)

class Z(object):
    def __init__(self,shape,*pack):
        self.shape = shape
        print('Z')
        super().__init__(*pack)

    def Print(self):
        print(self.shape)
        

class X(D,Z):
    same = 'naser2'
    age = None
    def __init__(self,breed, name, age,shape):
        self.breed = breed
        print('maman')
        pack = name, age, shape
        super().__init__(*pack)


    def Print(self):
        D.Print(self)
        Z.Print(self)
        print(same)
        # print("breed",self.breed)


a = X("diyam",55,77,66)
print(a.name)
print(a.age)
print(a.breed)
print(a.shape)
print(same)
print(a.same)
# out:
# maman
# Z
# 55
# 37
# khorshid
# naser
# naser2
# ######################################3
# و مفهوم(is part of)
# مفهوم (is a)


class Human(object):
    def __init__(self):
        self.hand = 'dast'

    def Print(self):
        print('human has:',self.hand)


class Hand(object):
    def __init__(self,color):
        self.color = color
        self.hand = Human()

    def Print(self):
        print(self.color)
        self.hand.Print()



s = Hand('red')
s.Print()
# out:
# red
# human has: dast
# #####################################

class New:
    def __init__(self,name):
        print(name)


    def __init__(self):
        self.name = 'siyamak'
        self.familyname = 'abasnezhad'
    
p=New()
print(p.name, p.familyname)
# out:
#siyamak abasnezhad


class New:
    def __init__(self):
        self.name = 'siyamak'
        self.familyname = 'abasnezhad'
    
    def __init__(self,name):
        print(name)


    
p=New('sisily')

# out:
# sisily
class Circle:
    def __init__(self,value):
        self.value = value
    @property
    def meg(self):
       return self.value /2


# >>> from property import Circle
# >>> d = Circle(10)
# >>> d.value
# 10
# >>> print(d.meg)
# 5.0
# >>>
# >>> d.meg = 10
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute
# >>>
    @meg.setter
    def meg(self,meg):
        self.value = meg * 2
# >>> from property import Circle
# >>> d = Circle(10)
# >>> d
# <property.Circle object at 0x000001AD09AA9668>
# >>> d.value
# 10
# >>> d.meg
# 5.0
# >>> d.meg = 20
# >>> d
# <property.Circle object at 0x000001AD09AA9668>
# >>> print(d.meg)
# 20.0
# >>> print(d.value)
# 40
# >>>
# ##############################################
class R(object):
    def __init__(self, initval=None, name ="var"):
        self.val = initval
        # self.name = name

    def __get__(self, obj, objtype):
        # print("ret...",self.name)
        return self.val

    def __set__(self, obj, val):
        # print('updated',self.name)
        self.val = val

class Spam(object):
    x = R(18, 'var "x" ')
    y = 5

x = Spam
print(x.y) 
print(x.x)
x.x = 14
print(x.x)
# out:
# 5
# 18
# 14
# ################################################
#  میتونیم به  این شکلم بنویسیم 
# ##############################################
class C(object):
    def __init__(self):
        self._name = None
    @property
    def name(self):
        print('@name.getter')
        return self._name
    @name.setter
    def name(self,val):
        print('@name.setter')
        self._name = val
    @name.deleter
    def name(self):
        print('@name.deleter')
        del self._name



x =C()
x.name
x.name = "siyamak"
print(x.name)
del x.name
print(x.name)
# out:
# @name.getter
# @name.setter
# @name.getter
# siyamak
# @name.deleter
# @name.getter
# Traceback (most recent call last):
#   File "tet.py", line 24, in <module>
#     print(x.name)
#   File "tet.py", line 7, in name
#     return self._name
# AttributeError: 'C' object has no attribute '_name'
# ####################################################
#####################################################
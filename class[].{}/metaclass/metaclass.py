# نیو بر میگردونه مقدار ابجکت و به اینیت میده
# #######################################
# ###################################################33
class Z(list):
    def __new__(*args,**kwargs):
        self = list.__new__(*args, **kwargs)
        return self
        
# >>> from test import Z
# >>> siyamak = Z([1 , 5 , "siyamak",55])
# >>> siyamak
# [1, 5, 'siyamak', 55]
# ##########################################33
class MyMeteClass(type):
    def __new__(cls, name, bases, dictionary):
        print('MyMetaClass -> new')
        print(cls)
        print(name)
        return type(name, (), dictionary)

class Bar(object):
    def Print(self):
        print('hi siyamak')

class Foo(Bar, metaclass = MyMeteClass):
    def __new__(cls,*args):
        print('ّFoo -> new')
        return object.__new__(cls) 

    def __init__(self, name):
        print('ّFoo -> init')
        self.name = name


x = Bar()
d = Foo("irin")
print(x.Print())
print(d.name)

# out:
# MyMetaClass -> new
# <class '__main__.MyMeteClass'>
# Foo
# ّFoo -> new
# ّFoo -> init
# hi siyamak
# irin
# d.Print() # ارور داریم بخاطر اینکه ما در مای متا کلاسمون بیسز و داخل تاپل و خالی گداشتیم
# فقط میتونیم x.Print بزنیم

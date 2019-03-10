# نیو بر میگردونه مقدار ابجکت و به اینیت میده
# #######################################
# ###################################################33


class Z(list):
    def __new__(*args, **kwargs):
        self = list.__new__(*args, **kwargs)
        return self

# >>> from test import Z
# >>> siyamak = Z([1 , 5 , "siyamak",55])
# >>> siyamak
# [1, 5, 'siyamak', 55]
# ##########################################33


class Z(tuple):
    def __new__(*args, **kwargs):
        self = tuple.__new__(*args, **kwargs)
        return self


s = Z([1, 5, "siyamak", 55])
print(s)

(1, 5, 'siyamak', 55)

################################################


class Z(set):
    def __new__(*args, **kwargs):
        self = set.__new__(*args, **kwargs)
        return self


s = Z([1, 5, "siyamak", 5, 55])
print(s)

# out:
# Z({1, 5, 'siyamak', 55})
##################################################


class MyMeteClass(type):
    def __new__(cls, name, bases, dictionary):
        print('MyMetaClass -> new')
        print(cls)
        print(name)
        return type(name, (), dictionary)


class Bar(object):
    def Print(self):
        print('hi siyamak')


class Foo(Bar, metaclass=MyMeteClass):
    def __new__(cls, *args):
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
#################################################333
class Z(type):
    def __new__(cls,name,*args):
        print(cls)
        print(name)

class Foo(object):
    def Print_r(self):
        print("hi siya")


    def __init__(self):
        self.name = "siya" * 10
       

x=Z("siyamak")
d = Foo()
d.Print_r()
print(d.name)
# out:
# <class '__main__.Z'>
# siyamak
# hi siya
# siyasiyasiyasiyasiyasiyasiyasiyasiyasiya
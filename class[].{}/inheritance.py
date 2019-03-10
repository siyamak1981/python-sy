class New():
    job="best programing in python"

    def print_it():
        print("blue_python")

    def __init__(self):
        self.language = "english"
    def getlanguage(self):
        return self.language
class Drive(New):
    def setlanguage(self):
        self.language='farsi'

a=Drive()
print(a.language)
print(a.getlanguage())
print(a.setlanguage())
print(a.getlanguage())
print(isinstance(a, Drive))
print(a.job)
print(a.print_it)
print(New.print_it())
g =New()
print(g.print_it())
print(a.print_it())
print(g.print_it())
print(a.print_it())
# ##################################
# english
# english
# None
# farsi
# True
# best programing in python
# <bound method New.print_it of <__main__.Drive object at 0x00000159212F3128>>
# blue_python
# TypeError:() takes 0 positional arguments but 1 was given
# TypeError:() takes 0 positional arguments but 1 was given
# <bound method New.print_it of <__main__.New object at 0x0000027932EAD940>>
# <bound method New.print_it of <__main__.Drive object at 0x0000027932EAD898>>
################################################################33
class N():
        klas = "siyamak is best pythonist"
        @property
        def o (self):
                print ("siyamak.py")
        
        def __init__(self,value=None, language=None):
                self.value = value
                self.language = "farsi"

        def P(self):
                return self.value
                return self.language
        @property
        def setlanguage(self):
                self.language = "eng"

        def getlanguage(self):
                return self.language
        

x = N()
print(x.klas)
x.o
x = N("diyana")
print(x.value,x.language)
x.setlanguage
print(x.getlanguage())
#######################
# out:
# siyamak is best pythonist
# siyamak.py
# diyana farsi
# eng
##############################33
class N():
        klas = "siyamak is best pythonist"
        @property
        def o (self):
                print ("siyamak.py")
        
        def __init__(self,value=None, language=None):
                self.value = value
                self.language = "farsi"

        def P(self):
                return self.value
                return self.language

        def getlanguage(self):
                return self.language
        
        @property
        def setlanguage(self):
                self.language = "eng"

x = N()
print(x.klas)
x.o
x = N("diyana")
print(x.value,x.language)
x.setlanguage
print(x.getlanguage())
# نتیجه مانند جواب قبلی هستش با تغییر ست و گت همان نتیجه رو داریم
#######################################3333


class Z(object):
        def __init__(self,name):
                self.name="5"
                # super().__init__(self)

class X(Z):
        def __init__(self):
                self.name = "siya"
                # super().__init__(self)

        @property
        def p(self):
                print ("siyamak:",self.name)
                # super().__init__(self)
                
v=X()
print (v.name)
v.p
# out
# 5
# siyamak: 5
# supper()وقتی میزاری زیر کلاس اونو حذف میکنه
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Z(object):
        def __init__(self,name):
                self.name="5"
            
class X(Z):
        def __init__(self):
                self.name = "siya"
                print ("siyamak:",self.name)
                super().__init__(self)


v=X()
print (v.name)
# out
# siyamak: siya
# 5
     
                
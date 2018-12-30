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
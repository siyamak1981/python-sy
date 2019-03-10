class Dog():
    _dogs = []
    def __init__(self, name):
        self.name = name
        Dog._dogs.append(name)

    def Print(self):
        print(Dog._dogs)

class Pittbul(Dog):
    _dogs = []
    def __init__(self, name):
        self.name = name
        Pittbul._dogs.append(name)
        super().__init__(name)

    def Print(self):
        print(Pittbul._dogs)


class Doberman(Dog):
    _dogs = []
    def __init__(self, name):
        self.name = name
        Doberman._dogs.append(name)
        super().__init__(name)

    def Print(self):
        print(Doberman._dogs)



ooo = Doberman("tuty")
ooo.Print()
ooo = Pittbul("susy")
ooo.Print()
ooo = Dog('dddii')
ooo.Print()
Dog.Print(Doberman)
Dog.Print(Pittbul)

# out:
# ['tuty']
# ['susy']
# ['tuty', 'susy', 'dddii']
# ['tuty', 'susy', 'dddii']
# ['tuty', 'susy', 'dddii']
# #########################################
#  (cls)همون نتیجه در پایین با نوشتن کد کمتر و گذاشتن کلاس متد و      
# ##########################################

class Dog():
    _dogs = []
    def __init__(self, name):
        self.name = name
        Dog._dogs.append(name)

   
    def Print(self):
        print(self._dogs)

class Pittbul(Dog):
    _dogs = []
    def __init__(self, name):
        self.name = name
        Pittbul._dogs.append(name)
        super().__init__(name)

    # def Print(self):
    #     print(Pittbul._dogs)


class Doberman(Dog):
    _dogs = []
    def __init__(self, name):
        self.name = name
        Doberman._dogs.append(name)
        super().__init__(name)

    # def Print(self):
    #     print(Doberman._dogs)



ooo = Doberman("tuty")
ooo.Print()
ooo = Pittbul("susy")
ooo.Print()
Dog.Print()

# out:
# ['tuty']
# ['susy']
# Traceback (most recent call last):
#   File "tet.py", line 93, in <module>
#     Dog.Print()
# TypeError: Print() missing 1 required positional argument: 'self'
# ############################################
# اینستند متد هستش ولی ارور داریم باید از کلاس متد استفاده کرد
# ##########################################
class Dog():
    _dogs = []
    def __init__(self, name):
        self.name = name
        Dog._dogs.append(name)

    @classmethod
    def Print(cls):
        print(cls._dogs)

class Pittbul(Dog):
    _dogs = []
    def __init__(self, name):
        self.name = name
        Pittbul._dogs.append(name)
        super().__init__(name)

  


class Doberman(Dog):
    _dogs = []
    def __init__(self, name):
        self.name = name
        Doberman._dogs.append(name)
        super().__init__(name)




ooo = Doberman("tuty")
ooo.Print()
ooo = Pittbul("susy")
ooo.Print()
Dog.Print()

# out:
# ['tuty']
# ['susy']
# ['tuty', 'susy']

# ############################################
# درستش بصورت زیر کاملا داینامیک
# ###########################################
class Dog():
    _dogs = []

    def __init__(self, name):
        if self.check_child():
            Dog._dogs.append(name)  # super
            self._dogs.append(name)  # subclass
            self.name = name
        else:
            raise NotImplementedError

    @classmethod
    def check_child(cls):
        if cls.__name__ in ('Dog'):
            return False
        else:
            return True

    @classmethod
    def Print(cls):
        print(cls._dogs)


class Pittbul(Dog):
    _dogs = []

    def __init__(self, name):
        super().__init__(name)


class Doberman(Dog):
    _dogs = []

    def __init__(self, name):
        super().__init__(name)


ooo = Doberman("tuty")
ooo.Print()
ooo = Pittbul("susy")
ooo.Print()
Dog.Print()
print(ooo.check_child())
print(ooo.name)
# i = Dog("ksd")

# out:
# ['tuty']
# ['susy']
# ['tuty', 'susy']
# True
# susy
##########################################33
class Dog():
    dogs = []
    
    def __init__(self,name):
        if self.check_child():
            Dog.dogs.append(name)
            self.name = name
        # else:
        #     raise NotImplementedError
    
    @classmethod
    def check_child(cls):
        if cls.__name__ in ('Dog'):
            return False
        else:
            return True

    @classmethod
    def Print(cls,name):
        print(cls.dogs)

class Pitbul(Dog):
    dogs = []
    def __init__(self,name):
        Pitbul.dogs.append(name)
        super().__init__(name)

    # def Print(self,name):
    #     print(Pitbul.dogs)


class Dober(Pitbul, Dog):
    doges = []
    def __init__(self,name):
        super().__init__(name)
        Dober.doges.append(name)


    # def Print(self,name):
    #     print(Dober.dogs)

        
# z = Pitbul("doberman")
# print(z.name)
# print(z.dogs)
# # z.Print()
# z.Print(Pitbul)

  
# z = Dober("shiyanlo")
# print(z.name)
# print(z.dogs)
# # z.Print()
# z.Print(Dober)

z = Dog('Dog')
print(z.name)
print(z.dogs)
# z.Print()
z.Print(Dog)

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

class Dog():
    dogs = []
    def __init__(self,name):
        self.name = name
        Dog.dogs.append(name)

    def bark(self, n):
        return '{} barked {}'.format(self.name, 'WOOF' * n)


# با ورود استاتیک متد ما دیگر نیاز به گذاشتن سلف نداریم و
#  تغییری اگه تو استنس داشته باشیم تو ج تغییری نداریم مثلا 
# s.dog_list
# Dog.dog_listتغییری در ج نداریم

    @staticmethod
    def dog_list():
        for dog in Dog.dogs:
            print(dog, end = '\n')

s = Dog('dober')
s = Dog('shiyanlo')
s = Dog('hhyanlo')
print(s.bark(5))
s.dog_list()
# بدون سلف تو داگ لیست ج نمیدهد اگه استاتیک متد نباشه
Dog.dog_list()
# بدون سلف ج میده تو داگ لیست
# out:
# hhyanlo barked WOOFWOOFWOOFWOOFWOOF
# dober
# shiyanlo
# hhyanlo
# dober
# shiyanlo
# hhyanlo
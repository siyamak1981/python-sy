class Dog(object):
    age = 0
    name = []
    def __init__(self, age = None,name = None ):
        Dog.age = age
        Dog.name.append(name) 

    def __str__(self):
        return_str = 'age :' + str(Dog.age)
        return_str += '\nname'+ str(Dog.name)
        return return_str


# out:
# >>> from tet import Dog
# >>> x = Dog(3, 'dober')
# >>> y = Dog(7,'shiyanlo')
# >>> print(y)
# age : 7
# name['dober', 'shiyanlo']
# >>> print(x)
# age : 7
# name['dober', 'shiyanlo']
# ##########################################


class Dog(object):
    
    def __init__(self, age = None,name = None ):
        self.age = age
        self.name = name 

    def __str__(self):
        return_str = 'age :' + str(self.age)
        return_str += '\nname'+ str(self.name)
        return return_str


# out:
# >>> from tet import Dog
# >>> x = Dog(2, ' shiyan')
# >>> y = Dog(3, ' dober')
# >>> print(x)
# age :2
# name shiyan
# >>> print(y)
# age :3
# name dober
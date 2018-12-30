class Reversedstr(str):
    
    def __new__( *args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[:-2:-1]
        return self

# ###################################فرقی نمیکنه در جواب بالا و پایین

class Reversedstr(str):
    
    def __new__(self,name, *args, **kwargs):
        self = str.__new__(self,name, *args, **kwargs)
        self = self[::-1]
        return self
#########################################33
class Reversedstr(str):
    
    def __new__(self,name):
        self = str.__new__(self,name)
        self = self[::-1]
        return self
# #############################################################
# >>>from reversedstr import Reversedstr
# >>>hi = Reversedstr("jhgj")
# >>>hi
# ###############################################################

# #############################################################
class String(str):
    def my_join(self, *args):
        return self.join(args)

s = String('')

# Python style:
s.join(['Hello ', 'world', '!'])
# My style:
s.my_join('Hello ', 'World', '!')

# Both return: 'Hello world!'

# Join list of strings using my style of join
l = ['Hello ', 'world', '!']
s.my_join(*l)
# returns: 'Hello world!'

# ######################################
class Z(object):
    def __init__(self, name):
        self.name= name
       

    def __str__(self):
        return (str(self.name))

s=Z("siyamak")
print(s)

# out:
# siyamak
# #############################################

def pack(*args):
    total = 66
    for num in args:
        total+=num
    return total
print(pack(5,4))  
# 75
# ############################
def pack1(base,*args):
    total = 66
    for num in args:
        total+=num
    return total
print(pack1(5,4))  
# 70
# ##################################
def func( a, *args):
     
   return args
#    return a
    

x=func("siyamak","diyana","sami")
print(len(x))
print(list(x))
# 2
# ['diyana', 'sami']
# ##################################
def pack2(base,*args):
    total = base
    for num in args:
        total+=num
    return total
print(pack2(5,8,4))
# args=8,4 >> base=5
# 17
# ############################################
def pack3(base,multiply="",*args,**kwargs):
    total = base
    for num in args:
        total+=num
    return total
print(pack3(5,4,8)) 
# 13
# ##################################################
# args* و kwargs** در پایتون
# http://mahdavipanah.com/blog/python-args-kwargs/
# ##################################################
def show_person_info(**kwargs):
    for key, value in kwargs.items():
        print('{} = {}'.format(key, value))
 
show_person_info(name='Hamidreza',
    family='Mahdavipanah',
    age='22') 
    
# name = Hamidreza
# family = Mahdavipanah
# age = 22
# #################################################
class String(str):
    def my_join(self, *args):
        return self.join(args)

s = String('')

# Python style:
print(s.join(['Hello ', 'world', '!']))
# Hello world!
# My style:
print(s.my_join('Hello ', 'World', '!'))
# Hello World!
# Both return: 'Hello world!'

# Join list of strings using my style of join
l = ['Hello ', 'world', '!']
print(s.my_join(*l))
# returns: 'Hello world!'
# Hello world!







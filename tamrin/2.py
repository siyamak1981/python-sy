# class N(type):
#     def __new__(cls, name, base):
#         print(cls)
#         # return(type(name,()))
#         print (name)
#         print (type(base))
# class Bar(object):
#     def Print(self):
#         print("hi siyamak")

# class Foo(Bar, N):
#     def __new__(cls,*args):
#         print (type(cls))
    
#     def __init__(cls, name):
#         self.name = name

# s = N("siyamak", {})
# a = Foo("eshgh")
# print(a.Print())


class C:
    def fun(self,x):
        print (x + 1)
a = C()
a.fun(2)
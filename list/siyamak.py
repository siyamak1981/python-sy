print("hello siyamak")
# hello siyamak
name="siyamak"
family="abasnezhad"
print(name+family)
# siyamakabasnezhad
print(name + family)
# siyamakabasnezhad
print(name + " " +family)
# siyamak abasnezhad
print(name, family)
# siyamak abasnezhad
# s="siyamak"
# y= 5
# z=s+y
# print(z)

s="siyamak"
y=str(6) 
l=s+y
print(l)
# siyamak6
# /////////

r="hello"*20
print(r)
# # hellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohello
# ///////
d='we are {}  {} in here'
print(d)
# we are {}  {} in here
print(d.format(5, 'human'))

# we are 5  human in here
# //////
n='we have {count} . {type} in here'
print(n.format(count=2, type='dog'))
# we have 2 . dog in here
# ////////
o='we have {count} . {type} in here'.format(count=3, type="cat")
print(o)
# we have 3 . cat in here
# //////
list
# ///////
mylist=["siyamak", "saed",55, 2, 4]
print(mylist)
# ['siyamak', 'saed', 55, 2, 4]
# ///////
mylist=["siyamak", "saed",55, 2, 4]
mylist+=[8,9]
print(mylist)
# ['siyamak', 'saed', 55, 2, 4, 8, 9]
# ///////
mylist=["siyamak", "saed",55, 2, 4]
mylist.append((7))
print(mylist)
# ['siyamak', 'saed', 55, 2, 4, 7]
# ///////
mylist=["siyamak", "saed",55, 2, 4]
mylist.extend([[7], "diyana", 1, {32}])
print(mylist)
# ['siyamak', 'saed', 55, 2, 4, [7], 'diyana', 1, {32}]
# ////////
mylist=["siyamak", "saed",55, 2, 4]
mylist.remove(55)
print(mylist)
# ['siyamak', 'saed', 2, 4]
# ////////
s=list("siyamak")
print(s)
# ['s', 'i', 'y', 'a', 'm', 'a', 'k']
# ////////
x="siyamak is great programer python".split()
print(x)
# ['siyamak', 'is', 'great', 'programer', 'python']
# //////
v="red:green:yellow".split()
print(v)
# ['red:green:yellow']
# /////////////////////////////
v="red:green:yellow".split(':')
print(v)
# ['red', 'green', 'yellow']
# ///////////////////////////
favorit=(["apple","orange"])
z="my favorit fruit is : " + ', '.join(favorit)
print(z)
# my favorit fruit is : apple, orange
# ////////
c= {"color":"red","age":32, "name":"siyamak"}
print(c)
# {'color': 'red', 'age': 32, 'name': 'siyamak'}
# ///////
v="red:green:yellow"
print(v)
# red:green:yellow
# ///////
irin=("elephan","cat")
l="my favorit animal is :{} ".format([ ", ".join(irin)])
print(l)
# my favorit animal is :['elephan, cat']
# ////////
alpha=["siyamak"]
print(alpha)
# ['siyamak']
# //////
alpha=list("siyamak")
print(alpha)
# ['s', 'i', 'y', 'a', 'm', 'a', 'k']
# //////
alpha=list("siyamak")
print(alpha[0])
# s
# ////////
k=list("siyamak")
print(k.index("i"))
# 1
# //////
k=list("siyamak")
del k[2]
print(k)
# ['s', 'i', 'a', 'm', 'a', 'k']
# //////
bool
# /////
print(bool(1))
# True
# ////
print(bool())
# # False
# /////
print(bool(0))
# False
# /////
print(bool(""))
# False
# /////
print(bool("siyamak"))
# True
# /////
print(bool([8, 2, 6]))
# True
# //////
print(bool(None))
# False
# ///////
print(5==5)
# True
# ///////
print(5==6)
# False
# /////
print(5<=5)
# True
# ///////
print(5<5)
# False
# ///////
print(5=="5")
# False
# ////////
print(5!=6)
# True
# ///////
print([]==[])
# True
# ////////
print([]==None)
# False
# ///////
print(""==[])
# False
# ///////
print(''==None)
# False
# ///////

















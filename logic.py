g=2000
if g>1000:
    print("its big" )
elif g<1500:
    print("its enough")
else:
    print("its ok")
    
# its big
# //////////////////////////////////////
date = ["sanday", "tuesday", "wensday"]
today = "monday"
if today in date:
    print("""today is monday""")
else:
    print("""today is else day""") 
    #    today is else day
# ////////////////////////////////////
date = ["sanday", "tuesday", "wensday"]
today = "monday"
if not today in date:
    print("today is monday")
else:
    print(" today is else day") 
    #   today is monday
# //////////////////////////////////////////
name = ["siyamak","saba", "diyana", "irin"]
print(type(name))
# ['siyamak', 'saba', 'diyana', 'irin']<class 'list'>
# ///////////////////////////////
del name
names=["siyamak","saba", "diyana", "irin", "mother"]
for name in names:
    print(name.upper())
    # SIYAMAK
# SABA
# DIYANA
# IRIN
# MOTHER
# /////////
x=10
while x:
    print(x)
    x-=1
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# ///////////
x = int(input("whats is ur age?\n"))
print(x)

# whats is ur age?
# 555
# 555
# //////////////////////////////////////////////////////
# *******************************************

try:
    count = int(input("enter ur number?\n"))
except ValueError:
    print("u have to write integer")
else:
    print("hello siyamak " * count)

# enter ur number?
# 5
# hello siyamak hello siyamak hello siyamak hello siyamak hello siyamak
# ****
# enter ur number?
# k
# u have to write integer




# enter ur number?
# 2
# hello siyamak hello siyamak



star = '*'
for i in range(6):
        print (star)
        star += '*'


# out:
# *
# **
# ***
# ****
# *****
# ******

x = int(input("enter ur number:\n"))
s = True
for ele in range(2,x):
    if x % ele == 0:
        s = False
        print("false")
        break
    else:
        print ("true")

# اعداد اول و چاپ کنه
# out
# enter ur number:
# 88
# false

def foo(n):
    space = 2 * n - 2
    i = 0
    for r in range(0, n):
        for s in range(0,space):
            print(end = ' ')
        space-=1
        for c in range(0, r + 1):
            print(i, end = " ")
            i +=1
        print(' ')
foo(int(input('whats urnumber? \n')))


# out
#       0 
#      1 2
#     3 4 5
#    6 7 8 9
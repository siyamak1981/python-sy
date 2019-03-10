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
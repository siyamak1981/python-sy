
# def his(item):
#     for i in range(6):
#         # i +=1
#         star = '*'
#         while (i < 6):
#             star +=str(1)
#         print (star)
      

# his([3,5,1,6,9])
        

# star = '*'
# for i in range(6):
#         print (star)
#         star += '*'


# out:
# *
# **
# ***
# ****
# *****
# ******

# def main():
#     # global count
#     # count = 0
#     n = input('shomararo vared kon?')
#     m = input('shomare tekrary?')

#     l=n.count(m)
#     print (l)
#     # return('shomare tekrari nist!')

# main()
####################################


# ###########################################333333
# class prim():
#     num=[]
#     for i in range(1,20):
#         num =input('enter num:')
#         if num % i ==0:
#             print(num)
#         i.append(num)
#         num=num+1
       


# v=prim()
# print (v.num)

import csv
exel = [['jessica', 1981]]
file = open('file.csv', 'w',newline= '')
csv.writer(file).writerows(exel)
ID = 'linux.py'
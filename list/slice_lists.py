u=["sina","sogayne", "siyamak"]
m=u[1:2]
print(m)
# ['sogayne']
# ##################################################
property=[1, 55, 414, 25, 125, 225, 666, 1, 22]
mutabel=property[2:5]
print(mutabel)
# [414, 25, 125]
# ##################################################
mutabel=property[3:]
print(mutabel)
# [25, 125, 225, 666, 1, 22]
# # ############################################
mutabel=property[4]
print(mutabel)
# 125
# #################################################
k=[1, 55, 414, 25, 125, 225, 666, 1, 22]
darkness=k[:]
# ====>> darkness save in new memory that is deposit of k for just to get [:] in front of k
print(darkness)
# [1, 55, 414, 25, 125, 225, 666, 1, 22]
darkness.sort()
print(darkness)
# [1, 1, 22, 25, 55, 125, 225, 414, 666]
print(k)
# [1, 55, 414, 25, 125, 225, 666, 1, 22]
# # ####################################################
# d=[1,5, 88, 9, 666, 77]
# # ====>>g have u be sure in first after that can be d otherwise u will enterface to the error====>>( d=g  NameError: name 'g' is not defined)
# g=d
# g.sort()
# print(d)
# print(g)
# # #######################################################
h=list(range(20))
print(h)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
oo=h[-8:]
print(oo)
# [12, 13, 14, 15, 16, 17, 18, 19]
# # #######################################
# del h[5]
# del h[10:13]
# h[2:4]=["siyamak","diyana"]

# # ########################################
# l=h[1:5]
# b=h[1::2]
# f=h[-1::-2]
# a=h[-2:6:-2]
# # ====>> a=h[-2:6:2] its mistake it cant move to positive
# print(l)
# print(b)
# print(f)
# print(a)
# # ####################################
# dd=["siyamak", "saeed", "saede","sadegh"]
# print(dd)












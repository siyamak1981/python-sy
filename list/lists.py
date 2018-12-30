# #################################
# lists are mutable (it mean that can replace with new member or parameter)(u can alter all of the items)
# ====>its not allocate for memory .in result it will be so optimasition
# w=list("one parameter have to be")
# strings are immutable
def bar (x, y):
    print(id(x), id(y))

    x += 1
    y.append('new')
    print(id(x), id(y))
bar(3, ["siyamak"])

# out:
# 140737312908176 1833336328904
# 140737312908208 1833336328904
# #########################################
# ###########################################################
# set() == lists  ====>>  !=dict{} tuple()   ????????
# ###########################################################
# *************************************************************
# (define error)
# ({[]}) it will be unhashable()  ======>>   h=({[1, 2, 3, 8, 9, 5]})
# a.remove([0])  =====>>ValueError: list.remove(x): x not in list
# *************************************************************
# ############################################################
#  extend=سومی رو نشون میده اگه سومی پرانتز باشه نشون نمیده.
# append=هر چی که  بعد از اولین پرانتز باشد را نشان میدهد
# ###########################################################
w=list("one parameter have to be")
print(w)
# ['o', 'n', 'e', ' ', 'p', 'a', 'r', 'a', 'm', 'e', 't', 'e', 'r', ' ', 'h', 'a', 'v', 'e', ' ', 't', 'o', ' ', 'b', 'e']
# //////
kf= ['kghj']
print(kf)
# ['kghj']
# //////////
lita=list(["atiyeh"])
print(lita)
# ['atiyeh']
# ///////
h=[1, 2, 3, 8, 9, 5]
print(h)
# [1, 2, 3, 8, 9, 5]
# ///////
h=h+[88]
print(h)
# [1, 2, 3, 8, 9, 5, 88]
# ///////
h+=[999]
print(h)
# [1, 2, 3, 8, 9, 5, 88, 999]
# ///////
h.append(55)
h.append(["maman"])
print(h)
# [1, 2, 3, 8, 9, 5, 88, 999, 55, ['maman']]
# //////
k=["siyamak", "maryam"]+[((((("saede")))))]
print(k)
# ['siyamak', 'maryam', 'saede']
# ======>None
# ///////
l=k.append(["sina"])
print(l)
# None
# ///////
k=["siyamak", "maryam"]+[{"hamideh"}]
print(k)
# ['siyamak', 'maryam', {'hamideh'}]
# ///////
a=[1,2,3]
a.extend("abf")
a.extend(["siu"])
a.extend({"shellow"})
print(a)
# [1, 2, 3, 'a', 'b', 'f', 'siu', 'shellow']
# //////
a.remove(2)
print(a)
# [1, 3, 'a', 'b', 'f', 'siu', 'shellow']
#/////////
a.extend(["siyamak"])
a.extend([["diyana"]])
a.extend([("exited")])
a.extend({" i love python"})
a.extend([{" i love pythonist",55555}])
print (a)
# [1, 3, 'a', 'b', 'f', 'siu', 'shellow', 'siyamak', ['diyana'], 'exited', ' i love python', {' i love pythonist', 55555}]
# /////
a.extend((((([" i am best developer about python3",77777])))))
print (a)
# [1, 3, 'a', 'b', 'f', 'siu', 'shellow', 'siyamak', ['diyana'], 'exited', ' i love python', {' i love pythonist', 55555}, ' i am best developer about python3', 77777]
# ///////////////
a.insert(0,{"i love my mother"})
print(a)
# [{'i love my mother'}, 1, 3, 'a', 'b', 'f', 'siu', 'shellow', 'siyamak', ['diyana'], 'exited',
#  ' i love python', {' i love pythonist', 55555}, ' i am best developer about python3', 77777]

# ###############################33
def show_person_info(**kwargs):
    for key, value in kwargs.items():
        print('{} = {}'.format(key, value))
 
   
show_person_info(name='Hamidreza',  family='Mahdavipanah',
    age='22')

# out:
# name = Hamidreza
# family = Mahdavipanah
# age = 22











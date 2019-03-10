# dict= is as same as lists are mutable.thay are random and it isnot to use andis[]
# u cant to use to plus in dictionary ===>{} + {} u will enterface with a typeerror bec thay are random
# ##############################################
# ====>> dictionary are iterable that u can do in it a proccess(پیمایش)
# ##############################
# #################################
fish=dict([{"first","sofi"},["lastname","paralel"]])
print(fish)
# {'sofi': 'first', 'lastname': 'paralel'}
# #################################
ff={ "name":"siyamak"}
print(ff)
ff={"family":"abasnezhad"}
print(ff, end='\n')
# {'name': 'siyamak'}
# {'family': 'abasnezhad'}
# ##############################
lesson={
    "cource":"advance python",
    "teacher":{"firstname":"siyamak","lastname":"abasnezhad"},
}
lesson["age"]=37
lesson.update({"cource":"advance python 3","job":"python", "teacher":{"firstname":"sosan", "lastname":"abasnezhad"}})

print(lesson)
# {'cource': 'advance python 3', 'teacher': {'firstname': 'sosan', 'lastname': 'abasnezhad'}, 'age':
# 37, 'job': 'python'}

# #########################################
print(lesson["cource"])
# advance python 3
print(lesson["teacher"]['lastname'])
# abasnezhad
# ###########################################
for dis in lesson:
    print(dis) 
# cource
# teacher
# age
# job
########################################
for dis in lesson:
    print(lesson[dis]) 
#     advance python 3
# {'firstname': 'sosan', 'lastname': 'abasnezhad'}
# 37
# python 
########################################
for item in lesson.items():
    print(item)
#     ('cource', 'advance python 3')
# ('teacher', {'firstname': 'sosan', 'lastname': 'abasnezhad'})
# ('age', 37)
# ('job', 'python')
# ############################################
for key in lesson.keys():
    print(key)
#     cource
# teacher
# age
# job
# ########################################
for v in lesson.values():
    print(v)
#     advance python 3
# {'firstname': 'sosan', 'lastname': 'abasnezhad'}
# 37
# python
# ########################################
lesson.clear()
print(lesson)
# {}
# # ###################################
u={1, 22 , 18 , 5 , 8 ,5 , 9 ,88}
print(u)
# {1, 5, 8, 9, 18, 22, 88}
u.remove(22)
print(u)
# {1, 5, 8, 9, 18, 88}
print(type(u))
# # =====>>> <class 'set'>
# # #############################
print(type(lesson))
# <class 'dict'>
# # ###############################
j={"(siyamak jango)"}
print(j)
# {'(siyamak jango)'}
# # #######################3
j={"siyamak jango"}
print(type(j))
# <class 'set'>
# ###################################

class New:
    def __init__(self):
        self.name = 'siyamak'
        self.familyname = 'abasnezhad'
    
    def Print(self):
        print(self. __dict__)
p=New()
print(p.Print())
# out:
# {'name': 'siyamak', 'familyname': 'abasnezhad'}


mydict = {}
while True:
    value = input ("pleaze insert your value : \n")
    key = input("please insert your key : \n")
    mydict[key] = value
    user=input("do u want to contenue write y else n to exit:\n")
    if user =="n":
        print("finished")
        print (mydict)
        break
    else:
        continue


# out
# please insert your key :
# rth
# do u want to contenue write y else n to exit:
# trh
# pleaze insert your value :
# rtg
# please insert your key :
# rt
# do u want to contenue write y else n to exit:
# n
# finished
# {'rth': 'rth', 'rt': 'rtg'}
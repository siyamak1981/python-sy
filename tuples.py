# #====>> tuple are immutable.thair functional are like lists .but so that lists are mutable 
# ===>thay arenot optimaiseing in use memory
# ====>داخل تاپلها فقط لیست قرار میگیرد اگر دیکشنری بزاریم سینتکس ارور خواهیم داشت
# ###################################################

tapu=(12, 1, 55, 6, 4)
print(tapu)
# (12, 1, 55, 6, 4)
# ################################
tapu = 1,2,2,55,58
print(tapu)
# (1, 2, 2, 55, 58)
# ###################################
r=(1,55, "siyamak", [77, 55, 123])
print(r)
# (1, 55, 'siyamak', [77, 55, 123])
# #################################
print(r[3][1])
# 55
# ####################################
mm=(1,55, "siyamak",[{"age":37,"siyamak":"name"}, 554, 663])
print(mm[3][0])
# {'age': 37, 'siyamak': 'name'}
print(mm[1])
# 55
print(len(mm))
# 4
# ######################################
# ########==========>>> TypeError: unhashable type: 'list'
# hh=(1,55, "siyamak",{["age","siyamak", 55, 123]})
# print(hh)
# ##########################
# mm[2]="irin"
# =======>>>TypeError: 'tuple' object does not support item assignment(غیر قابل تغییر)
# (فقط تو لیستا رو میتونی تغییر بدی)
# ################################
mm=5
print(mm)
# 5
# #############################################








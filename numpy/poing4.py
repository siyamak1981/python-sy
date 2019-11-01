import numpy as np

# x = np.array([1,8,7,6])
# y= np.array([44,55,66,88])
# z = np.append(x, y)
# print(z)



# در نظر داشته باشید که متد append، آرایه را به یک بعد تغییر می‌دهد، پس برای اضافه کردن به آرایه‌های دو بعدی از متد vstack و برای آرایه‌های ۳ بُعد به بالا بَعد از استفاده از متد append، بُعد آن را با متد reshape به بُعد مورد نظر خود تغییر دهید.


# g = np.array([
#     (1, 2, 4),
#     (4, 8, 9),
#     (7, 8, 5),

# ]
# )
# z = np.array([1,8,7])
# h=np.vstack((z, g))
# print(h)



f = np.array([55,6,7,8,1,4,5,77,88])
g = np.array([
    (1, 2, 4),
   

]
)
print(np.append(g,f).reshape(4,1,3))



f = np.array([55,6,7,8,1,4,5,77,88])
# print(np.insert(f, 3,1000))
# print(np.delete(f, 2))
# print(f.reshape(3,3))
replaced_f = f
replaced_f[0]=8888555
print(replaced_f)
import sys
import numpy as np
import time
import matplotlib.pyplot as plt



l  = np.array((1, 8 , 9))
print(l)
x = np.array((44,55,88,77,99,555,444,888,999,))
g = np.array([
    (1, 2, 4),
    (4, 8, 9),
    (7, 8, 5),

]
)
print(np.array(g).ndim)
print(np.array(x).ndim)
print(np.array(l).ndim)


print(np.array(l).dtype)
print(np.array(x).dtype)
print(np.array(g).dtype)


# linspace: با دادن حد بالا، حد پایین و تعداد اعداد، یک ترکیب خطی از اعدادِ بین دو حد، ایجاد می‌کند.
u  = np.linspace(1, 8 , 9)
print(u)



# plt.plot(l)
# plt.show()

# ones: به ابعاد دلخواه ۱ ایجاد می‌کند.

p = np.ones((3,4))
print(p)

# zeros: به ابعاد دلخواه ۰ ایجاد می‌کند.

k= np.zeros((3,4))
print(k)

f = np.random.random((6,8))
print(f)


# متد normal، توزیع نرمالی از اعداد تصادفی ‌تولید می‌کند. این متد ۳ پارامتر اصلی می‌پذیرد: میانگین، انحراف معیار و تعداد داده‌ها


m = np.random.normal((20,10,1000))
print(m)

plt.scatter(m,np.arange(1,len(m)+1,1),color="cyan")
plt.show()
plt.plot(m,color="red")

# full: آرایه‌ را با یک مقدار به ابعاد دلخواه پر می‌کند.
c = np.full((4,2), 5.45)
plt.plot(c,color="black")
plt.show()
# print(c)

# numpy از توابع مختلفی پشتیبانی می‌کند. برای مثال تابع سینوس به صورت زیر است:
d = np.arange(0,3*np.pi,0.1)
y = np.sin(d)
plt.plot(y, linewidth=10, color="green")
plt.show()
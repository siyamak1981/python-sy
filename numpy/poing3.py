import numpy as np
# توصیه می‌شود برای ساخت آرایه ۳ بعد به بالا، ابتدای آرایه تک بعدی بسازید و سپس با استفاده از متد reshape ابعاد آن را عوض کنید:

x = np.arange(50).reshape(5,2,5)
print(x)
print(x[1,1,2])
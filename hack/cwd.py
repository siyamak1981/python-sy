import os
# print(os.getcwd())
# print(os.listdir())
# print(os.listdir('/'))
# print(os.listdir('.'))
# مسیر فعلی
# print(os.listdir('/eng'))
# دایرکتوری
# print(os.path)
# print (os.path.isdir("  .git "))
# فایل وجود دارد؟
for item in os.listdir('.'):
    if os.path.isdir(item):
        print("directory is:",item)
    elif os.path.isfile(item):
        print ("not directory:",item)


# not directory: color.py
# not directory: fork.py
# not directory: tamrin.py
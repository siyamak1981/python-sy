
try:
    1/0
except BaseException as e:
    print(e)
    print(type(e))
    print('خطا', e)
    print(e.__doc__)



# out:
# division by zero
# <class 'ZeroDivisionError'>
# خطا division by zero
# Second argument to a division or modulo operation was zero.
# ##############################################

x = 12
if type(x) == int:
    raise NameError


# out:
#     raise NameError
# NameError

assert 'x' in locals().keys()
# out:
# AssertionError
# ####################################3
# حرکت اکسپشنها از جز به کل نمی تو نیم بیس اکسپشن و بنو یسیم بعد نیم ارور و بزاریم باید ار کوچک به بزرگ باشد
# ###########################################
import time 

def main():
    run()
    make_delay()


def make_delay():
    
    time.sleep(3)
    print('ready to exite..')
    for i in range(10):
        time.sleep(1)
        print('.',end = '')
    print("all done...") 
    time.sleep(2)
    exit(0)


def run():
        try:
            while True:
                print('try again siyamak')

        except KeyboardInterrupt:
            print('KeyboardInterrupt')


if __name__ == "__main__":
    main()

# out:
# try again siyamak
# try again siyamak
# try again siyamak
# try again siyamak
# try again siyamak
# KeyboardInterrupt
# ready to exite..
# ..........all done...

# #################################3
import zipfile

zf = zipfile.ZipFile('p.zip','r')
dic = open('py.txt','rb')
counter = 0
for i in dic:
    passsword= i.strip()
    try:
        zf.extractall(pwd = passsword)
        break
    except:
        counter+=1
        print('{} checked'.format(counter))

print('[ + ] Password:', passsword)
# out:
# 1 checked
# 2 checked
# 3 checked
# 4 checked
# [ + ] Password: b'python'
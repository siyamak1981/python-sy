

### Decorator ###

#Log message decorator

## Seperation concerns
def logme(func):
    import logging
    logging.basicConfig(level = logging.DEBUG)

    def inner():
        logging.debug('called {}'.format(func.__name__))
        return func


    inner()
# ##################################################
# out:
# >>> def h():
# ...     print(9)
# ...
# >>> h()
# 9
# >>> h = logme(h)
# DEBUG:root:called h

# ################################################333
# or در نهایت با دکوریشن به اینصورت میشه که ما کمتر کد میزنیم
# >>> @logme
# ... def h():
# ...     print(5555)
# ...
# DEBUG:root:called h
# ######################################################33

from functools import wraps

def logme(func):
    import logging
    logging.basicConfig(level = logging.DEBUG)

    @wraps(func)
    def inner(*args, **kwargs):
        logging.debug("called {} with args {} and these kwargs {}".format(func.__name__,
        args, kwargs))
        return func(*args, **kwargs)

    # inner.__doc__ = func.__doc__   نیاز نداریم @wrap(func)  که این دوخط روبرو با گذاشتن 
    # inner.__name__ = func.__name__
    
    return inner
# ##############################################
    
# >>> @logme
# ... def sub(x, y, switch = False):
# ...     """ subtract x and y """
# ...        
# ...
# >>> sub(8, 3)
# DEBUG:root:called sub with args (8, 3) and these kwargs {}
# 5
# >>> sub.__doc__
# ' subtract x and y '
# >>> sub.__name__
# 'sub'
# ###################################

# >>> @logme
# ... def sub(x, y, switch = True):
# ...     return x - y if not switch else y - x
# ...
# >>> sub(8, 3)
# DEBUG:root:called sub with args (8, 3) and these kwargs {}
# -5
# ############################################################
def foo (f):
        def boo(name):
                return '<b>' + f(name) +'</b>'
        return boo
def get_name(name):
        return name
x=foo(get_name)("siyamak")
print (x)
# out:
# <b>siyamak</b>
# ===>فو رو صدا میزنم ورودی فو تابع اف بود
#  که در واقه همون گت نیم ما بود که مقدار فو رو به ما بر میگرئونه
#  و اگر با ورودی نیم صدا زده بشه مقدار تابع نیم رو به ما بر میگردونه
# ###############################
def foo (f):
        def boo(name):
                return '<b>' + f(name) +'</b>'
        return boo

@foo 
# decorators
def get_name(name):
        return name

x=get_name("siyamak")
print (x)
# out:
# <b>siyamak</b>
# ##########################33333




import time
def foo(f):
        def bar(*args):
                print(*args)
                start = time.clock()
                r = f(*args)
                stop= time.clock()
                print(stop-start)
                return r

        return bar
 
@foo
def bala(x):
        if x <=0:
                return -1
        bala(x-1)

x =bala(15)
print(x)


# out:
# 15
# test.py:6: DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
#   start = time.clock()
# 14
# 13
# 12
# 11
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# test.py:8: DeprecationWarning: time.clock has been deprecated in Python 3.3
#  and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
#   stop= time.clock()
# 7.799999999999474e-05
# 0.0002680749999999926
# 0.00039656999999999887
# 0.0005267080000000007
# 0.000658076999999993
# 0.0007812360000000046
# 0.0009019310000000086
# 0.0010291939999999972
# 0.0011925840000000104
# 0.002089998999999995
# 0.002221778999999993
# 0.002394611000000005
# 0.002563749000000004
# 0.0027386340000000037
# 0.0028897080000000047
# 0.003275605000000001
# None
def outer():
    number = 5
    def inner():
        print(number)

    inner()
# out
# >>> outer()
# 5
# ##################################
def apply(func, x, y):
    return func(x, y)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

print(apply(sub, 5, 5))
print(apply(add, 2, 2))

# out
# 0
# 4
# ####################################
def close():
    x = 55
    def outher():
        print(x)

    return outher


closure = close()
closure()

# out
# 55

# ##########################################333
def add_to_five(num):
    
    def outher():
        print(num+5)

    return outher

fifteen = add_to_five(10)
fifteen()

# out:
# 15

# ###########################################################3
# ############################################################
# ################################################## 


import time

def log(username,**args):

    if args.get('login'):
        print('wlc %s',username)
        print(time.ctime())
    
    elif args.get('logout'):
        print('%s logout',username)
        print(time.ctime())

log('siyamak', login = True)
log('siyamak', login = False, logout = True)
# ################################################
import datetime

def log(username,**args):

    if args.get('login'):
        print('wlc %s',username)
        print(datetime.datetime.now())
    
    elif args.get('logout'):
        print('%s logout',username)
        print(datetime.datetime.now())

log('siyamak', login = True)
log('siyamak', login = False, logout = True)

# out:
# wlc %s siyamak
# Sun Dec  9 16:37:43 2018
# %s logout siyamak
# Sun Dec  9 16:37:43 2018
# wlc %s siyamak
# 2018-12-09 16:37:43.752873
# %s logout siyamak
# 2018-12-09 16:37:43.753878
################################################
def foo(prompt, retire = 3 , complain= ' yes or no'):
    while True:
        ok = input(prompt)
        if ok in ('yes' , 'y' , 'ok'):
                print (True)
        elif ok in ('No', 'n' , 'no'):
                print  (False)
        retire -=1 
        if retire <0:
                return None
            
        print(complain)

foo("what do y write ?", retire=0)
# ##########################################33
def foo(j):
    
    for d in j:
        return d
    

x=foo('siyamak')

for i in x:
    print(i)

# out:s
# ######################
def foo(j):

    for d in j:
        yield d
    

x=foo('siyamak')
for i in x:
    print(i)
# out:
# s
# i
# y
# a
# m
# a
# k
# #########################################

var = 12
print(locals())
print (id(var))
def x():
    var = "str"
    print(id(var))
    return var

print(var)

# out:
# >>> from test import x
# {'__name__': 'test', '__doc__': None, '__package__': '', '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001F7F16FCF98>, '__spec__': ModuleSpec(name='test', loader=<_frozen_importlib_external.SourceFileLoader object at 0x000001F7F16FCF98>, origin='D:\\website\\python37\\python.sa\\siyamak\\test.py'), '__file__': 'D:\\website\\python37\\python.sa\\siyamak\\test.py', '__cached__': 'D:\\website\\python37\\python.sa\\siyamak\\__pycache__\\test.cpython-37.pyc', '__builtins__': {'__name__': 'builtins', '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", '__package__': '', '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>), '__build_class__': <built-in function __build_class__>, '__import__': <built-in function __import__>, 'abs': <built-in function abs>, 'all': <built-in function all>, 'any': <built-in function any>, 'ascii': <built-in function ascii>, 'bin': <built-in function bin>, 'breakpoint': <built-in function breakpoint>, 'callable': <built-in function callable>, 'chr': <built-in function chr>, 'compile': <built-in function compile>, 'delattr': <built-in function delattr>, 'dir': <built-in function dir>, 'divmod': <built-in function divmod>, 'eval': <built-in function eval>, 'exec': <built-in function exec>, 'format': <built-in function format>, 'getattr': <built-in function getattr>, 'globals': <built-in function globals>, 'hasattr': <built-in function hasattr>, 'hash': <built-in function hash>, 'hex': <built-in function hex>, 'id': <built-in function id>, 'input': <built-in function input>, 'isinstance': <built-in function isinstance>, 'issubclass': <built-in function issubclass>, 'iter': <built-in function iter>, 'len': <built-in function len>, 'locals': <built-in function locals>, 'max': <built-in function max>, 'min': <built-in function min>, 'next': <built-in function next>, 'oct': <built-in function oct>, 'ord': <built-in function ord>, 'pow': <built-in function pow>, 'print': <built-in function print>, 'repr': <built-in function repr>, 'round': <built-in function
# round>, 'setattr': <built-in function setattr>, 'sorted': <built-in function sorted>, 'sum': <built-in function sum>, 'vars': <built-in function vars>, 'None': None, 'Ellipsis': Ellipsis, 'NotImplemented': NotImplemented, 'False': False, 'True': True, 'bool': <class 'bool'>, 'memoryview': <class 'memoryview'>, 'bytearray': <class 'bytearray'>, 'bytes': <class 'bytes'>, 'classmethod': <class 'classmethod'>, 'complex': <class 'complex'>, 'dict': <class 'dict'>, 'enumerate': <class 'enumerate'>, 'filter': <class 'filter'>, 'float': <class 'float'>, 'frozenset': <class 'frozenset'>, 'property': <class 'property'>, 'int': <class 'int'>, 'list': <class 'list'>, 'map': <class 'map'>, 'object': <class 'object'>, 'range': <class 'range'>, 'reversed': <class 'reversed'>, 'set': <class 'set'>, 'slice': <class 'slice'>, 'staticmethod': <class 'staticmethod'>, 'str': <class 'str'>, 'super': <class 'super'>, 'tuple': <class 'tuple'>, 'type': <class 'type'>, 'zip': <class 'zip'>, '__debug__': True, 'BaseException': <class 'BaseException'>, 'Exception': <class 'Exception'>, 'TypeError': <class 'TypeError'>, 'StopAsyncIteration': <class 'StopAsyncIteration'>, 'StopIteration': <class 'StopIteration'>, 'GeneratorExit': <class 'GeneratorExit'>, 'SystemExit': <class 'SystemExit'>, 'KeyboardInterrupt': <class 'KeyboardInterrupt'>, 'ImportError': <class 'ImportError'>, 'ModuleNotFoundError': <class 'ModuleNotFoundError'>, 'OSError': <class 'OSError'>, 'EnvironmentError': <class 'OSError'>, 'IOError': <class 'OSError'>, 'WindowsError': <class 'OSError'>, 'EOFError': <class 'EOFError'>, 'RuntimeError': <class 'RuntimeError'>, 'RecursionError': <class 'RecursionError'>, 'NotImplementedError': <class 'NotImplementedError'>, 'NameError': <class 'NameError'>, 'UnboundLocalError': <class 'UnboundLocalError'>, 'AttributeError': <class 'AttributeError'>, 'SyntaxError': <class 'SyntaxError'>, 'IndentationError': <class 'IndentationError'>, 'TabError': <class 'TabError'>, 'LookupError': <class 'LookupError'>, 'IndexError': <class 'IndexError'>, 'KeyError': <class 'KeyError'>, 'ValueError': <class 'ValueError'>, 'UnicodeError': <class 'UnicodeError'>, 'UnicodeEncodeError': <class 'UnicodeEncodeError'>, 'UnicodeDecodeError': <class 'UnicodeDecodeError'>, 'UnicodeTranslateError': <class 'UnicodeTranslateError'>, 'AssertionError': <class 'AssertionError'>, 'ArithmeticError': <class 'ArithmeticError'>, 'FloatingPointError': <class 'FloatingPointError'>, 'OverflowError': <class 'OverflowError'>, 'ZeroDivisionError': <class 'ZeroDivisionError'>, 'SystemError': <class 'SystemError'>, 'ReferenceError': <class 'ReferenceError'>, 'MemoryError': <class 'MemoryError'>, 'BufferError': <class 'BufferError'>, 'Warning': <class 'Warning'>, 'UserWarning': <class 'UserWarning'>, 'DeprecationWarning': <class 'DeprecationWarning'>, 'PendingDeprecationWarning': <class 'PendingDeprecationWarning'>, 'SyntaxWarning': <class
# 'SyntaxWarning'>, 'RuntimeWarning': <class 'RuntimeWarning'>, 'FutureWarning': <class 'FutureWarning'>, 'ImportWarning': <class 'ImportWarning'>, 'UnicodeWarning': <class 'UnicodeWarning'>, 'BytesWarning': <class 'BytesWarning'>, 'ResourceWarning': <class 'ResourceWarning'>, 'ConnectionError': <class 'ConnectionError'>, 'BlockingIOError': <class 'BlockingIOError'>, 'BrokenPipeError': <class 'BrokenPipeError'>, 'ChildProcessError': <class 'ChildProcessError'>, 'ConnectionAbortedError': <class 'ConnectionAbortedError'>, 'ConnectionRefusedError': <class 'ConnectionRefusedError'>, 'ConnectionResetError': <class 'ConnectionResetError'>, 'FileExistsError': <class 'FileExistsError'>, 'FileNotFoundError': <class 'FileNotFoundError'>, 'IsADirectoryError': <class 'IsADirectoryError'>, 'NotADirectoryError': <class 'NotADirectoryError'>, 'InterruptedError': <class 'InterruptedError'>, 'PermissionError': <class 'PermissionError'>, 'ProcessLookupError': <class 'ProcessLookupError'>, 'TimeoutError': <class 'TimeoutError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-Z plus Return to exit, 'exit': Use exit() or Ctrl-Z plus Return to exit, 'copyright': Copyright (c) 2001-2018 Python Software Foundation.
# All Rights Reserved.

# Copyright (c) 2000 BeOpen.com.
# All Rights Reserved.

# Copyright (c) 1995-2001 Corporation for National Research Initiatives.
# All Rights Reserved.

# Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
# All Rights Reserved., 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
#     for supporting Python development.  See www.python.org for more information., 'license': Type license() to see the full license text, 'help': Type help() for interactive help, or help(object) for help about object.}, 'var': 12}
# 140737312908464
# 12
# >>> x()
# 2164384369216
# 'str'
# #####################################

x = 12
def foo():
        # global x
        x = "str"
        print(x)
foo()
print(x)

def bar():
        globals()['x']='int'
        print(x)
bar() 
print(x) 
# out:
# str
# 12
# int
# int
# #######################################

def foo():
        def bar():
                return('bar()')
        return bar


# out:
# >>> foo()
# <function foo.<locals>.bar at 0x000001A1AEACC268>
# >>> foo()()
# 'bar()'
# #############################################3
def foo():
        return ('hi siyamak')
        

def call_foo(bibi):
        return bibi()

s = call_foo(foo)
print(s)
# out:
# hi siyamak
# ###################################
def foo(name):
        return ('hi siyamak' + name)
        

def call_foo(b):
        return b(" \ baby")

s = call_foo(foo)
print(s)

# out:
# hi siyamak \ baby
# #############################

def foo():
        def bar():
                print ("baby")
                return bar
        return bar
x=foo()()()()
print(x)

# out:

# baby
# baby
# baby
# <function foo.<locals>.bar at 0x0000014BFD1A8A60>
# ###############################################
def foo(x, **kwargs):
        if kwargs.get('plus'):
                return bar(x, **kwargs) + 3
        bar(x, **kwargs)
def bar(x, **kwargs):
        if kwargs.get('sq'):
                return x**2
        if kwargs.get('cb'):
                return x**3
        return -1
k=foo(5,sq=True , plus= True )
l=foo(9,cb=True , plus= True )
print(k)
print(l)
# out:
# 28
# 732
# ######################################3
def foo(num):
        if num<=0:
                return 0 
        foo(num-1)
        print(num)
foo(5)
# out:
# 1
# 2
# 3
# 4
# 5
# ####################################3333
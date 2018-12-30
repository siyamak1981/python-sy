# >>> import datetime
# >>> dir(datetime)
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

# >>> datetime.datetime.now()
# datetime.datetime(2018, 12, 6, 12, 16, 56, 63651)

# >>> start= datetime.datetime.now()
# >>> start
# datetime.datetime(2018, 12, 6, 12, 18, 34, 512699)

# >>> start= start.replace(hour=9 , minute=8, second= 0, microsecond = 0)
# >>> start
# datetime.datetime(2018, 12, 6, 9, 8)

# >>> worktime = datetime.datetime.now() - start
# >>> worktime
# datetime.timedelta(seconds=12092, microseconds=418049)

# >>> dir(worktime)
# ['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__floordiv__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 'days', 'max', 'microseconds', 'min', 'resolution', 'seconds', 'total_seconds']

# >>> hourswork = round(worktime.seconds/3600)
# >>> hourswork
# 3

# >>> datetime.timedelta(hours = 9)
# datetime.timedelta(seconds=32400)

# >>> datetime.timedelta(days=3) + datetime.datetime.now()
# datetime.datetime(2018, 12, 9, 12, 50, 17, 394407)




# >>> hour = datetime.timedelta(hours = 1)
# >>> hour
# datetime.timedelta(seconds=3600)
# >>> workday = hour * 8
# >>> workday
# datetime.timedelta(seconds=28800)
# >>> x = round(workday.seconds/3600)
# >>> x
# 8



# >>> tomarrow = datetime.datetime.now().replace(hour = 9, minute = 0, second = 0)
# >>> tomarrow
# datetime.datetime(2018, 12, 6, 9, 0, 0, 166856)
# >>> v = tomarrow + workday
# >>> v
# datetime.datetime(2018, 12, 6, 17, 0, 0, 166856)


# >>> appointment = datetime.timedelta(minutes = 45)
# >>> start = datetime.datetime(2018, 10, 10, 18, 0, 0, 0)
# >>> end = appointment + start
# >>> end
# datetime.datetime(2018, 10, 10, 18, 45)




# >>> import datetime
# >>> now = datetime.datetime.now()
# >>> now
# datetime.datetime(2018, 12, 6, 13, 21, 40, 579990)

# >>> now.strftime('%B %d')
# 'December 06'
# >>> now.strftime('%b %d')
# 'Dec 06'
# >>> now.strftime('%m %d')
# '12 06'
# >>>


# >>>  now.strftime('%Y %m %d')
#   File "<stdin>", line 1
#     now.strftime('%Y %m %d')
#     ^
# IndentationError: unexpected indent
# >>> now.strftime('%y %m %d')
# '18 12 06'
# >>> now.strftime('%y_%m %d')
# '18_12 06'



# >>> birthday = datetime.datetime.strptime('1981_01_01 09:00', '%Y_%m_%d %H:%M')
# >>> birthday
# datetime.datetime(1981, 1, 1, 9, 0)

import dis

def sum():
   vara = 10
   varb = 20

   sum = vara + varb
   print ("vara + varb = %d" % sum)

# Call dis function for the function.

dis.dis(sum)



# out 


# 13           0 LOAD_CONST               1 (10)
#               2 STORE_FAST               0 (vara)

#  14           4 LOAD_CONST               2 (20)
#               6 STORE_FAST               1 (varb)

#  16           8 LOAD_FAST                0 (vara)
#              10 LOAD_FAST                1 (varb)
#              12 BINARY_ADD
#              14 STORE_FAST               2 (sum)

#  17          16 LOAD_GLOBAL              0 (print)
#              18 LOAD_CONST               3 ('vara + varb = %d')
#              20 LOAD_FAST                2 (sum)
#              22 BINARY_MODULO
#              24 CALL_FUNCTION            1
#              26 POP_TOP
#              28 LOAD_CONST               0 (None)
#              30 RETURN_VALUE

# (
# Dismodule Disassembler پایتون است. این کد کدهای بایت را به فرمت دیگری تبدیل می کند که برای مصرف انسان مناسب تر است.

# شما می توانید disassembler را از خط فرمان اجرا کنید. این اسکریپت داده شده را کامپایل می کند و کدهای بایت جدا شده را به STDOUT چاپ می کند. شما همچنین می توانید از DIS به عنوان یک ماژول استفاده کنید. تابع discharges یک کلاس، متد، تابع یا شیء کد را به عنوان یک آرگومان واحد می برد.)
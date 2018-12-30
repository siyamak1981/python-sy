import copy
import filledlist
class Filledlist(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count):
            self.append(copy.copy(value))

# ##############################3##############333333
# >>> import filledlist
fl = filledlist.Filledlist(12, 3)
print(fl)
# [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
# [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
fl2=filledlist.Filledlist(2, [2,6, 5],{5,1, 8})
print(fl2)
# [[2, 6, 5], [2, 6, 5]]
# [[2, 6, 5], [2, 6, 5]]
print(fl2[0][1])
# 6
# 6

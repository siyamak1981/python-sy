# =====>>>>overloading<<<<<====== #
class New:
    def __init__(self,name):
        print(name)


    def __init__(self):
        self.name = 'siyamak'
        self.familyname = 'abasnezhad'
    
p=New()
print(p.name, p.familyname)
# out:
#siyamak abasnezhad


class New:
    def __init__(self):
        self.name = 'siyamak'
        self.familyname = 'abasnezhad'
    
    def __init__(self,name):
        print(name)
  
p=New('sisily')

# out:
# sisily
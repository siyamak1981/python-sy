

def packages(firstname=None,**kwargs):
    # print("hi {}".format(firstname))
    print(kwargs)
packages(firstname="siyamak",age=37, country="iran")
# {'age': 37, 'country': 'iran'}
# ###########################################################
def unpackages(firstname=None, lastname=None):
    if firstname and lastname:
       print("hi {} '{}'".format(firstname,lastname))
    else:
        print("there is not")
unpackages(**{"firstname":"siyamak", "lastname":"abasnezhad"})
# hi siyamak 'abasnezhad'
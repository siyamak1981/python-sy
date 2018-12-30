# def remember(thing):

#     file = open('database.txt','a')
#     file.write(thing + '\n')
    

#     file.close()

# if __name__ == "__main__":
#         remember(input("what do u remeber?"))


# ######################################################
import sys


def remember(thing):
    # open file

    with open('database.txt', 'a') as file:
        # 'w' => for writing truncating the file first
        # 'a' => for writing appending to the end of the file
        file.write(thing + "\n")


def show():
    # open file
    with open('database.txt', 'r') as file:
        for line in file:
            # print out each line in file
            print(line)


if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()
    else:
        remember(' '.join(sys.argv[1:]))
  
# $ python remember.py soda11
# ##############################
# $ python remember.py --list
# siyamak
# saeed
# sami
# ##############################
# >>> file = open('database.txt')
# >>> file
# <_io.TextIOWrapper name='database.txt' mode='r' encoding='cp1256'>
# >>> file.read(2)
# 'si'
# >>> file.read()
# 'yamak\nsaeed\nsami\n\n'
# >>> file.seek()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: seek() takes at least 1 argument (0 given)
# >>> file.seek(0)
# 0
# >>> file.read()
# 'siyamak\nsaeed\nsami\n\n'
# ##########################################
# >>> s = file.readlines()
# >>> len(s)
# 0
# ###########################################
# >>> file.seek(0)
# 0
# >>> s = file.readlines()
# >>> len(s)
# 4
# >>> for d in s:
# ...     print(d)
# ...
# siyamak
# saeed
# sami
# ################################3
# >>> for d in s:
# ...     print(d[::-1])
# ...
# kamayis
# deeas
# imas
# #######################################

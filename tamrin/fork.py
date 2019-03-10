# import os
# for item in os.listdir('.'):
#     if os.path.isdir(item):
#         print("directory is:",item)
#     elif os.path.isfile(item):
# 
#         print ("not directory:",item)
import os
# import fork
# print (type(os.getpid()))
def child_proc():
    print ("child proces is exit")
    print ("child proces exit %d pid " % os.getpid())

def parent_proc():
    print ("parent_proc is started %d pid"%os.getpid())
    fork_proc = os.fork()
    if (fork_proc == 0):
        child_proc()
    else :
        print ("child proc forked %d pid"%fork_pros)



parent_proc()
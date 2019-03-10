import thread
def g (ID):
    print ("thread %d start"%ID)

for num in range(1,5):
    thread.start_new_thread(g, tuple([num]))

while (True):
    pass
import signal
def control_signal(signal, frame):
    print ("pls exit")
signal.signal(signal.SIGINT,control_signal)
while (True):
    pass
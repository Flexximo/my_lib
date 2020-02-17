import threading

def threadInfo(data):
    call(data)
def call(data):
    print("Tread %s : %s" % (threading.current_thread(), data))
if __name__ == "__main__":
    call("Main program")
    for i in range(4):
        p = threading.Thread(target=threadInfo, args=("Function %s" % i,))
        p.start()
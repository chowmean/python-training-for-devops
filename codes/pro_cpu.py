import multiprocessing
import logging
import time
from datetime import datetime

def process_function(name):
    #logging.info("Thread %s: starting", name)
    for i in range (10000):
        a = (i*i)
        b = (i*i)+1
    #logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    start_time = datetime.now()
    format = "%(asctime)s: %(message)s"
    #logging.basicConfig(format=format, level=logging.INFO,
    #                    datefmt="%H:%M:%S")

    #logging.info("Main    : before creating thread")
    for i in range (100):
        x = multiprocessing.Process(target=process_function, args=(i, )) 
        x.start()
        x.join()
    #y = threading.Thread(target=thread_function, args=(1,))
    #logging.info("Main    : before running thread")
    #x.start()
    #y.start()
    #logging.info("Main    : wait for the thread to finish")
    # x.join()
    #logging.info("Main    : all done")
    end_time = datetime.now()
    print(end_time-start_time)

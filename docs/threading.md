# Threading and multiprocessing in Python

Threading module implments basic threading in python. Using threading is not an easy task. Threading wants you to write your code in a concurrent design so that it can run parallely on your CPU.

Now there are two things: What is difference between concurrency and parallelism and what about these in python. 

## What is difference between concurrency and parallelism. 

In simple word concurrency is a property of your code and parallelisn is property of your runtime. This means concurrency you have to implement in your code and if that code runs in parallel or not on CPU is parallelism. 

## Concurrency and parallelism in python.

You can write concurrent code in python but it will never run in parallel. The cause if GIL which doesn't let you run code in parallel in python. Though you will have the illusion of these things running in parallel if you are doing I/O intensive tasks. 

Now lets implement a threaded program in python 

## Threading implementation

We will use threading library to make our program run in parallel. 
<pre>
import logging
import threading
import time
from datetime import datetime

def function(name):
    logging.info("Thread %s: starting", name)
    for i in range (1000):
        a = (i*i)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    for i in range (3):
        x = threading.Thread(target=function, args=(i,))
        x.start()
        x.join()
</pre>

In the above code we have imported thread. Then created 3 threads and started them and after that joined them so that the execute will proceed after that only once all the threads are completed. 

Now let us see how we will do the same using multiprocessing. 

## Multiprocessing in python

Multiprocessing instead of creating threads create a new process which itself is heavier. Let use multiprocessing in above program.

<pre>
import logging
import multiprocessing
import time
from datetime import datetime

def function(name):
    logging.info("Thread %s: starting", name)
    for i in range (1000):
        a = (i*i)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    for i in range (3):
        x = multiprocessing.Process(target=function, args=(i, ))
        x.start()
        x.join()
</pre>

## Threading vs Multiprocessing in python

Threading in python is helpful in IO bound process and Multithreading in case of CPU bound. We will see the comparision of CPU bound process to see the difference between the execution time of mutlithreaded program and multiprocess program. 



<pre>
#multiprocessing version
import multiprocessing
import logging
import time
from datetime import datetime

def process_function(name):
    for i in range (10000):
        a = (i*i)
        b = (i*i)+1

if __name__ == "__main__":
    start_time = datetime.now()
    format = "%(asctime)s: %(message)s"

    for i in range (100):
        x = multiprocessing.Process(target=process_function, args=(i, ))
        x.start()
        x.join()
    end_time = datetime.now()
    print(end_time-start_time)
</pre>


<pre>
#Multithreaded version
import logging
import threading
import time
from datetime import datetime

def thread_function(name):
    for i in range (10000):
        a = (i*i)
        b = (i*i)+1

if __name__ == "__main__":
    start_time = datetime.now()
    format = "%(asctime)s: %(message)s"
    
    for i in range (100):
        x = threading.Thread(target=thread_function, args=(i,))
        x.start()
        x.join()
    
    end_time = datetime.now()
    print(end_time-start_time)

</pre>


When you run this program you can see the time taken by both the program to complete the execution. Try and explain why the time difference happened. 

Thinking in term of context swtiches, size of thread and process and how GIL works will help you in defining why the time difference in there. 
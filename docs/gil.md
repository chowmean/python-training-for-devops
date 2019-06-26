# GIL: Global Interpreter Lock

Gil is a mutex lock in python which allows only one thread to execute at a time. This is why python is single threaded application. So if your program is simgle threaded python will perform as equal to any other language. But when it comes to multithreading and executing threads in parallel, it is not possible in python

## Why GIL?

Python uses reference counting for memory management. What it does is it keeps track of all the variables that are created and wheather they are being used in the program now or not. If their is no reference for those variables. The python garbage collector kicks in and removes that variable from the heap. 

Now for this reference counting to work properly it need to be safe from race conditions. That is two threads try to change the reference count. If that happens that can lead to memory leak. This reference count can be kept safe by locking all the data structures that are shared accross the threads. 

Now if we lock these data structures. It means multiple locks will exist which can lead to problems like deadlock. Also it will decrease performance as aquisition and release of locks will happen quite frequently. 

GIL is a single lock which says that execution of any python byte code requires the interpreter lock. This prevents the above problem but makes the python single threaded. 

## Why only GIL as solution?

Python has been around since the days when operating systems did not have a concept of threads. Python was designed to be easy-to-use in order to make development quicker and more and more developers started using it.

A lot of extensions were being written for the existing C libraries whose features were needed in Python. To prevent inconsistent changes, these C extensions required a thread-safe memory management which the GIL provided.

The GIL is simple to implement and was easily added to Python. It provides a performance increase to single-threaded programs as only one lock needs to be managed.

C libraries that were not thread-safe became easier to integrate. And these C extensions became one of the reasons why Python was readily adopted by different communities.


## Impacts?

There are two kinds of multithreaded programs.

* I/O bound program : Programs that wait for input/output from user, file, database, network etc. These sometimes have to wait alot. 
* CPU bound program : These programs are the one which does high computational tasks. 

We will see how python works in both these cases. 

In case of CPU bound programs the multithreading will not make any difference as the only one thread will execute. Infact you can see performance degrading for these cases. 

In case of IO bound process the multithreading will increase performance as IO bound process mostly wait for the input or output to be provided to them and they are in waiting state. Aquiring and releasing lock for these kind of process doesn't cause problem cause when one thread may got the output or input the others may still be waiting for the event. 


## Work around?

If you want to make use of all your core in pytho program instead of going for multithreading go for <b>multiprocessing</b>. Each process gets its own python interpretor this the GIL is applied on only that process and hence you can do lot of work in parallel. 

Read more about GIL [here](https://realpython.com/python-gil/)
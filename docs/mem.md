# Memory Management 

This concept deals with the way python manages memory, how it assigns memory, how it cleans memory and garbage collect. 

An OS-specific virtual memory manager carves out a chunk of memory for the Python process.

Python uses a portion of the memory for internal use and non-object memory. The other portion is dedicated to object storage (your int, dict, and the like).

## Garbage Collection

Python interpretor keeps the reference count of all the variables, if reference count of any variable becomes 0. That variable is garbage collected.

If you want to read more about it read here
[memory management in python](https://realpython.com/python-memory-management/)
# Generators

Generators are just like normal functions, what makes functions generators in yield statement instead of return statement. 

## What is yield?

Yield is a key word that is used to return the value only, the difference is it is used to induce the lazy processing capability. What is does is it returns the state of the functions at that time and save it locally so that it can be resumed from there in the next iteration. 
So it actually doesn't generate any value but save the function state so that it can be generated on the run time. Have a look at the code below 

<pre>
def testgen():
    for i in range(10000):
        yield i
</pre>

So what is happening here is we have created a generator using yeild. Yeild creates an itertor by itself so it works out of the box from with `for-in`

In the above function we have created a generator that is generating list from 0,9999. 


## Advantages of generators

Generator have following advantages
- They don't process at the same time but does lazy loading so when the value is required it gets executed and gets the data. 
- They help a lot in saving memory by not generating and saving things in memory all at once.


### Memory Efficient and lazy processing.
Lets have a look at the code below. 

<pre>
from sys import getsizeof

def tesgen():
        for i in range(10000):
                yield i

b = [x for x in range(10000)]
print(getsizeof(b))

a = tesgen()
print(getsizeof(a))
</pre>

If you can run this program you can see the difference between memory consumption in both the cases. Lets discuss why there is so much difference in memroy consumption here. 

Memory difference is because there is no acutal calculation and storing of the values in the memory. 

### Infinite Sequence of data

It is easy to have an infinite sequence of data with generators because of the memory advantage otherwise for infite sequence of data you need infinite RAM. 


### Iterator by default

Generators automatically define `__iter__` and `__next__`. Thus these can be used directly with `for-in` and has iterators. You can get the iterators using `iter` key word.

## Python generator experssion

<pre>
a = (x**2 for x in my_list)
</pre>
Above code creates generator, what you need to do this is use `()` with your normal expression. 

This was introduction to generators. These are very powerful and you can use them to accomplish different tasks. Now its upto you how you will dig deeper and use it. 

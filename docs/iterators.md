# Iterators 

Generally, iterators are used to iterate over a list of objects. We use iterators without knowing we are using it. Look at the below example

<pre>
a = [1,2,4,5,6,7,8]
for i in a:
	print(i)
</pre>

Here we have used iterator behind the scenes of `for-in` to loop over a list. 

## How to create Iterators?

Iterators consists of two important functions

<pre>
__iter__
</pre>

<pre>
__next__
</pre>

If your class has these two functions written properly it can be used as iterator and can be used with `for-in`.

## Iterator Visualization

Lets take a list and try to iterate over it with iterator. 

<pre>
a = [1,2,3,4,5,6,7]
it = iter(a)  #same as it = a.__iter__()
print(it.__next__())
</pre>

Everytime you print if will print the next value in list till it reaches stop iteration exception. Now lets try and create iterator classes. 


## Basic Iterator Example.

<pre>
class Iterator:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

a = Iterator("asdad")

for item in a: 
	print(item)
</pre>


Here what we are doing is creating and object of Iterator class which has iter which returns itself and and next which returns the values. This is then used in `for-in` to demonstrate iterator working.

This iterator will keep on printing whatever value you will provide it forever. It will not break. Since in `__next__` function we are just returning the value itself and not chagning anything else. Ideally it should change some value which defines when this iterator will stop. 

Let us now try and write an iterator which will loop over out list of numbers and print it. 

## Creating List iterators

<pre>
class NumberIterator:
    def __init__(self, value):
        self.value = value
        self.index = 0
        self.length = len(value)

    def __iter__(self):
        return self

    def __next__(self):
        
        if self.index<self.length:
            returnvalue = self.value[self.index]
            self.index = self.index + 1
            return returnvalue
        if self.index >= self.length:
            raise StopIteration

a=[1,2,3,4,5,6,7,8,9]
a=NumberIterator(a)
for item in a:
	print(item)
</pre> 

As you can see now in `__next__` function we are checking if we reached will the end of the len or not if yes we are stopping the iteration. 

This is how iterator for list may be implemented. 

Now lets try and see if manully getting an iterator will work with our class?

<pre>
a=[1,2,3,4,5,6,7,8,9]
a=RepeaterNumber(a)
it = a.__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
</pre>

If it works we have learned the basic of how iterator works. 
Iterate if you still have problems. :)
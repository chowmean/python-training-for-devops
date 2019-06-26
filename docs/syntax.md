# About python




## Blocks in python

While in most of the langauges blocks are defined using brackets like {}, (), [] but in python blocks are defined using spaces that is the piece of code that has the same spaces from the start of line belong to that contiguous block. 

Example: 

<pre>
for(int i=0;i<=20;i++){	//block start  
	console.log(i)
}	//block end
</pre>

This is javascript example of printing number from one to 20

<pre>
i=0
while i<=20: 	#block start
	print(i)
				#block end
</pre>

This is python style of the same. 

### Why are Blocks important?

Blocks are important because variables scoping depends a lot on them. Variable defined inside a block will only be accessible from inside the block only.

## Variables 
#### Python Variable Name Rules
- Must begin with a letter (a - z, A - B) or underscore (_)
- Other characters can be letters, numbers or _
- Case Sensitive
- Can be any (reasonable) length
- There are some reserved words which you cannot use as a variable name because Python uses them for other things.

####Good Variable Name
- Choose meaningful name instead of short name. roll_no is better than rn.
- Maintain the length of a variable name. Roll_no_of_a-student is too long?
- Be consistent; roll_no or RollNo
- Begin a variable name with an underscore(_) character for a special case.


Since python in not static typed language you do not need to define the type of variables. 


## Loops

### For

<pre>
i=0
for i < 10:
	print(i)
	i++
</pre>

### While

<pre>
i=0
while i<10:
	print(i)
	i++
</pre>

### Loop through objects

<pre>
a = [1,2,3,4,5,6,7]
for i in a:
	print(i)
</pre>

<pre>

a=[{"name":"qw"},{"name":"qwe"}]

for i in a:
	print(a["name"])
</pre>

## Functions

<pre>

def function_add(var1, var2, var3):
	do_some_work
	return var1+var2+var3
</pre>

### Default arguements in functions

<pre>
def function_default_arg(var1, var2, var3=10):
	return var1+var2+var3
</pre>

Here if no value is specified for var3 it will be 10 by default so you can call it like below. It also shows us a form of polymorphism which we will see later in this tutorial.
#Concept of Object Oriented Programming


### Objects

Everything in python are objects. Even if you initialize a variable with 1. 1 is a object of type int. 

### Classes

Classes are combination of variables and functions. Classes define a type of any object. An example of class in below

<pre>
class employee():	
  
  __phone_number=""
	
	def __init__(name, age):
		self.name = name
		self.age = age
	
	def get_age():
		return self.age
	
	def set_age(value):
		self.age = value
	
	def get_name():
		return self.name
	
	def set_phone(value):
		self.__phone_number = value

</pre>

This is an example of class, Here we have private variable __phone_number, which cannot be ediited by anyone else but functions inside the class. __init__() is a constructor which is used to initialize the class. 

### Inheritance
The capability of a class to derive properties and characteristics from another class is called Inheritance. Inheritance is one of the most important feature of Object Oriented Programming.
Sub Class: The class that inherits properties from another class is called Sub class or Derived Class.
Super Class: The class whose properties are inherited by sub class is called Base Class or Super class.

<pre>

class Employee():	
  
	__phone_number="0000000000"
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def get_age(self):
		return self.age
	
	def set_age(self,value):
		self.age = value
	
	def get_name(self):
		return self.name
	
	def set_phone(self,value):
		self.__phone_number = value

	def get_phone(self):
		return self.__phone_number 

	def set_phone(self, value):
		self.__phone_number = value

class VIP(Employee):

	def get_phone(self):
		return "************"

	def get_vip_access(self):
		return "access_granted"

if __name__ == '__main__':

	#Simple Employee 
	emp = Employee("gaurav", 12)
	print(emp.get_phone())
	emp.set_phone("89628363**")
	print(emp.get_phone())

	#Vip employee inherting employee properties
	vip = VIP("Venky", 54)

	#Overriden method hides phone number
	print(vip.get_phone())

	#Extra added function. 
	print(vip.get_vip_access())

	#This function calls the inherited method.
	print(vip.get_name())
	

</pre>

### Encapsulation

Encapsulation is a way to hide some of the variables of the class to be not accessible from outside the class. In other languages there are class members like private and protected but in python there is no such concept. Instead you can define a private class member like this

<pre>

class Employee():	
  
	__phone_number="0000000000"
</pre>

Here __phone_number is a private class member and cannot be accessible from outside the class. You cannot access this variable like below. 

<pre>

a = Employee()
a.__phone_number
</pre>

To access these variables you have to write getter and setter function for these. Which can do the basic checks before setting the variables. 

<pre>

class Employee():	
  
	__phone_number="0000000000"

	def get_phone(self):
		return self.__phone_number

	def set_phone(self, value):
		self.__phone_number = value

</pre>
#### Use of Encapsulation?

Say you have a class User where you have age and password class members. Here you will not want anyone outside the class to see password. Also you want to apply some check before setting the password. This can be done using this. Look at the code below.

<pre>

class User():
	
	__password=""

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def set_password(password):
		if password_check(password):
			self.__password=password
</pre>


### Polymorphism

Polymorphism means having many forms. In programming it means that same function names can be used for different types of work. 

<pre>
def add(x, y, z = 0):  
    return x + y+z 
  
# Driver code  
print(add(2, 3)) 
print(add(2, 3, 4)) 

</pre>
Here function add has two forms. One is when it takes two arguements where the third one itself is 0. Other is when it takes 3 variables. This is very basic example of polymorphism
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
	

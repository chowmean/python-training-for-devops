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

if __name__ == '__main__':
	e = Employee("gaurav", 12)
	print(e.get_phone())
	e.set_phone("89628363**")
	print(e.get_phone())
	

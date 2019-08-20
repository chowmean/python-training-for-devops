# class Repeater:
#     def __init__(self, value):
#         self.value = value

#     def __iter__(self):
#         return self

#     def __next__(self):
#         return self.value

# a = Repeater("asdad")

# for item in a: 
# 	print(item)



class RepeaterNumber:
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
a=RepeaterNumber(a)
for item in a:
	print(item)

a=[1,2,3,4,5,6,7,8,9]
a=RepeaterNumber(a)
it = a.__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
class Stack:
	def __init__(self,MAX=100):
		self.MAX=MAX
		self.data=list()		
	def push(self,value):
		if(len(self.data)==self.MAX):
			raise StackMemoryFullException
		self.data.append(value)
		
	def pop(self):
		if(len(self.data)==0):
			raise StackEmptyException
		temp=self.data[-1]
		self.data=self.data[:-1]
		return(temp)
	
	def peek(self):
		if(len(self.data)==0):
			raise StackEmptyException
		return(self.data[-1])


class StackMemoryFullException(Exception):
	def __str__(self):
		return("Your Stack memory is almost full");
	
class StackEmptyException(Exception):
	def __str__(self):
		return("Your Stack is Empty")
		
u=Stack(1)
u.push("hi")
u.push("hi")

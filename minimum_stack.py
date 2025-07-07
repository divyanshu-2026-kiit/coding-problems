# leetcode - 155 | min-stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,val):
        if len(self.stack) == 0: 
            self.stack.append([val,val])
        else:
            minimum = min(self.stack[-1][1],val)
            self.stack.append([val,minimum])

    def getmini(self):
        if len(self.stack) == 0:
            return 0
        return self.stack[-1][1]
    
    def display(self):
        print(self.stack)

    def pop_stack(self):
        self.stack.pop() 

    def top(self):
        return self.stack[-1]       
    

# check if the methods work correctly
stack1 = Stack()
stack1.push(5)
stack1.push(6) 
stack1.push(2) 
stack1.push(10) 
stack1.push(4) 
stack1.display()
result1 = stack1.top()
print(result1)
stack1.push(6) 
stack1.push(7)
stack1.display()
result2 = stack1.getmini() 
print(result2)
stack1.push(1) 
stack1.push(9) 
stack1.pop_stack()
stack1.display()
result3 = stack1.getmini()
print(result3)
stack1.push(20)
stack1.push(35)
stack1.display()
result4 = stack1.top()
print(result4)
stack1.pop_stack()
stack1.display()
result5 = stack1.getmini() 
print(result5)
result6 = stack1.top()
print(result6)

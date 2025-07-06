# push
#pop
# insert at specific pos
# delete from specific pos
#slicing
# display

class Stack:
    def __init__(self):
        self.lst = []

    # push
    def push_at_last(self,val):
        self.lst.append(val)
        return self.lst
        
    def pop_from_last(self):
        if self.lst is None:
            return "pop is not possible as list is empty"
        self.lst.pop()
        return self.lst

    def push_at_specific_index(self,index,val):
        length = len(self.lst)
        if length < index:
            return "index out of bound"
        if self.lst is None:
            return "list is empty "
        self.lst.insert(index,val)
        return self.lst

    def pop_specific_value(self,val): 
        if self.lst is None:
            return "pop is not possible as list is empty"
        self.lst.pop(val)
        return self.lst
    
    def slicing(self,start,end):
        length = len(self.lst)
        if start > length and end > length:
            return "index out of bound"
        if end < start:
            return "end index is less than start index"
        if self.lst is None:
            return "list is empty"
        return self.lst[start:end+1]

        
    def display(self):
        if self.lst is None:
            return "list is empty"
        return self.lst

obj = Stack()
for i in range(1,15):
    obj.push_at_last(i)
result1 = obj.display()
print(result1)
obj.pop_from_last()
result2 = obj.display()
print(result2)
obj.push_at_specific_index(4,100)
result3 = obj.display()
print(result3)
obj.pop_specific_value(5)
result4 = obj.display()
print(result4)
result6 =  obj.slicing(6,10)
print(result6)




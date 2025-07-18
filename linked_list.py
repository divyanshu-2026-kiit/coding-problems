# linked list
#insertion
#deletion
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
# insert at beginning
    def insert_at_beginning(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            new_node.next = current
            self.head = new_node


# insert at last
    def insert_at_last(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

# insert at specific position
    def  insert_at_specific_position(self,val,position):
        new_node = Node(val)
        if self.head is None:
            return "linkedlist is empty"
        if position == 0:
            current = self.head
            new_node.next = current
            self.head = new_node
        else:
            count = 0
            previous = None
            current = self.head
            while current.next is not None and count < position:
                previous = current
                current = current.next
                count+= 1
            previous.next = new_node
            new_node.next = current            

# delete from beginning
    def delete_from_beginning(self):
        if self.head is None:
            return "list is empty"
        else:
            self.head = self.head.next

# delete at last    
    def delete_at_last(self):
        if self.head is None:
            return "list is empty"
        else:
            if self.head.next is None:
                self.head = None
                return 
            current = self.head
            previous = None
            while current.next is not None:
                previous = current
                current = current.next    
            previous.next = None
            
# delete from specific pos
    def delete_from_specific_position(self,position):
        if self.head  is None:
            return "list is empty"
        if position == 0:
            self.head = self.head.next
        else:
            current = self.head
            previous = None
            count = 0
            while current.next is not None and count < position:
                previous = current
                current = current.next
                count +=1
                if current.next is None:
                    previous.next = None
                    return
            previous.next = current.next  

    def display(self):
        if self.head is None:
            return "linked list is empty"
        else:
            current = self.head
            while current is not None:
                print(current.val,end =" ")
                current = current.next


       
linked_list = linkedlist()
linked_list.insert_at_beginning(5)  
linked_list.insert_at_beginning(6) 
linked_list.insert_at_last(7)
linked_list.insert_at_specific_position(10,2)
linked_list.delete_from_specific_position(0)
linked_list.display()
linked_list.delete_from_beginning()
linked_list.display()
linked_list.delete_at_last()
linked_list.display() 
linked_list.delete_at_last()
linked_list.delete_at_last()
result = linked_list.delete_at_last()
print(result)
print(linked_list.display()) 


                




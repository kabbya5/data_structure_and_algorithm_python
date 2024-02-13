class Node:
    def __init__(self,value) :
        self.value = value 
        self.next = None 

class LinkList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node
        self.length = 1 
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def print(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next 

    def pop(self):
        if self.length == 0:
            return  None
        
        pre = self.head 
        temp = self.head 

        while(temp.next):
            pre = temp 
            temp = temp.next 
            
        self.tail = pre 
        self.tail.next = None 

        self.length -= 1

        if self.length == 0:
            self.head = None 
            self.tail = None 

        print(temp.value)


list = LinkList(4)
list.append(3)
list.append(7)
list.pop()
list.pop()
list.pop()
list.pop()
list.print()
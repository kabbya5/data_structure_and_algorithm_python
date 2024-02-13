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


list = LinkList(4)
list.append(3)
list.append(7)
list.print()

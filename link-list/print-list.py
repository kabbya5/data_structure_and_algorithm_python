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
    
    def print(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next 


list = LinkList(4)

list.print();
class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
        self.prev = None

class DoublyLinkedList:
    
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node 
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail  = new_node 
            
        self.length += 1
        return True 


    def print_list(self):
        temp = self.head 

        while temp is not None:
            print(temp.value)
            temp = temp.next


list = DoublyLinkedList(5)
list.append(4)
list.print_list()
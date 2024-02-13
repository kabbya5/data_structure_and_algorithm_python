class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.next = None
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def pop(self):
        if self.length == 0:
            return None 
        temp = self.head 
        pre = self.head 

        while(temp.next):
            pre = temp 
            temp = temp.next
        self.tail = pre 
        self.tail.next = None
        self.length -= 1
        
    
    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next


listed_1 = LinkedList(2)
listed_1.append(4)
listed_1.append(6)
listed_1.pop()
listed_1.print_list()

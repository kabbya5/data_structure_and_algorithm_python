class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

class Queue:
    def __init__(self,value):
        new_node  = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print(self):
        temp = self.first 
        
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self,value):
        new_node = Node(value)

        if self.first is None:
            self.first = new_node
            self.last = new_node 
        else:
            self.last.next = new_node
            self.last = new_node 

        self.length += 1


queue = Queue(4)
queue.enqueue(5)
queue.print()
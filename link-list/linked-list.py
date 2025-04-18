class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 


class LinkedList:
    def __init__(self,value):
        new_node = Node(value) 
        self.head = new_node 
        self.tail = new_node 
        self.length = 1 

    def insert(self,value):
        new_node = Node(value) 
        
        if self.head is None:
            self.head = new_node 
            self.tail = new_node 
        else:
            self.tail.next = new_node 
            self.tail = new_node 

        self.length += 1 

    def insert_first(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else:
            new_node.next = self.head 
            self.head = new_node 
            new_node = None 

        self.length += 1 

    
    def display(self):
        curr = self.head 

        while(curr):
            print(curr.value)
            curr = curr.next 

    def reverse(self):
        prev = None
        current = self.head 

        while(current):
            next_node = current.next 
            current.next = prev 
            prev = current 
            current = next_node 
        
        return  prev
    
    def print_list(self, head):  # we pass head as argument
        current = head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
   


ll = LinkedList(5)
ll.insert(10)
ll.insert_first(20)
ll.insert_first(30)
ll.display()
reversed_head = ll.reverse()
ll.print_list(reversed_head)






        

    

    

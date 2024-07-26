class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 



class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node 
        self.height = 1

    def push(self,value):
        new_node = Node(value)

        if(self.height == 0):
            self.top = new_node
        else:
            new_node.next = self.top 
            self.top = new_node

        self.height += 1


    def print(self):
        temp = self.top 
        while temp is not None:
            print(temp.value)
            temp = temp.next 


my_stack = Stack(4)
my_stack.push(5)
my_stack.print() 

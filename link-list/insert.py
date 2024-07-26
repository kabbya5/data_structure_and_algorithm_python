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

    def prepend(self,value):
        new_node = Node(value)
        if(self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head = new_node
        
        self.length += 1

        return True
    
    def pop_first(self):
        if self.length == 0:
            return None 
        
        temp = self.head 
        self.head = self.head.next 
        temp.next = None 
        self.length -= 1 

        if self.length == 0:
            self.tail = None 

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head 
        for _ in range(index):
            temp = temp.next 
        return temp
    
    def set_value(self,index,value):
        if index < 0:
            return False 
        
        if index == 0:
            self.head.value = value 
        
        temp = self.head 
        current_index = 0; 

        while temp.next:
            if(current_index == index):
                temp.value = value 
                return True 
            
            temp = temp.next 
            current_index += 1 
        
        return False 
    

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next 

        new_node.prev = before 
        new_node.next = after 

        before.next = new_node 
        after.prev = new_node

        self.length += 1

        return True
        


list = LinkList(4)
list.append(3)
list.append(7)
list.prepend(1)
list.prepend(2)
list.prepend(7)
list.print()
print('new List')
list.set_value(3,11)
list.insert(2,5)
list.print()

class Node:
    def __init__(self,value):
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

    def appendArray(self,lists):
        for value in lists:
            new_node = Node(value) 
            if self.head is None:
                self.head = new_node
                self.tail = new_node 
            else:
                self.tail.next = new_node 
                self.tail = new_node
            self.length += 1
                    
            
    def middle(self):
        slow = self.head 
        fast = self.head 

        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next

    def remove_duplicates(self):
        values = set() 
        previous = None 
        current = self.head 

        while current:
            if current.value in values:
                previous.next = current.next 
                self.length  -= 1

            else:
                values.add(current.value)
                previous = current 
            
            current = current.next
           


        

list = LinkList(1)
array = [2,3,1,4,5]
list.appendArray(array)

list.print()
list.middle()



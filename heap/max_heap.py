from collections import deque

class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None 
        self.parent = None 


class MaxHeap:
    def __init__(self):
        self.root = None 
        self.nodes = [] 

    def insert(self, value):
        new_node =  Node(value)

        if not self.root:
            self.root = new_node 
            self.nodes.append(new_node) 
        else:
            parent = self.nodes[0] 
            new_node.parent = parent 

            if not parent.left:
                parent.left = new_node 
            elif not parent.right:
                parent.right  = new_node 
                self.nodes.pop(0) 
            
            self.nodes.append(new_node) 
            self._bubble_up(new_node)

    def _bubble_up(self, node):
        while node.parent and node.parent.value < node.value:
            node.value, node.parent.value = node.parent.value, node.value 
            node = node.parent 

    def extract_max(self):
        if not self.root:
            return None
        max_value = self.root.value 

        if len(self.nodes) == 1:
            self.root = None 
            return max_value
        
        last_node = self.nodes[-1] 
        self.root.value = last_node.value 

        if last_node.parent.right == last_node:
            last_node.parent.right = None 
        else:
            last_node.parent.left = None 

        self.nodes.pop() 

        self._bubble_down(self.root)

        return max_value 
    
    def _bubble_down(self,node):
        while node:
            largest = node 

            if node.left and node.left.value > largest.value:
                largest = node.left 
            
            if node.right and node.right.value > largest.value:
                largest = node.right 

            if largest == node:
                break 

            node.value, largest.value = largest.value, node.value 
            node = largest 


    def print_level_order(self):
        if not self.root:
            print("Empty Heap")
            return

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.value, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(30)
heap.insert(15)
print("Before extract:")
heap.print_level_order()

max_val = heap.extract_max()
print("Extracted max:", max_val)

print("After extract:")
heap.print_level_order()
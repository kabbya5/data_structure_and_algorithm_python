class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None 
        self.parent = None 

class MinHeap:
    def __init__(self):
        self.root = None 
        self.size = 0 

    def insert(self,value):
        new_node = Node(value)
        self.size += 1 

        if self.root is None:
            self.root = new_node 
        else:
            queue = [self.root]

            while queue:
                current = queue.pop(0)
                if current.left is None:
                    current.left = new_node 
                    new_node.parent = current 
                    break 
                else:
                    queue.append(current.left)
                
                if current.right is None:
                    current.right = new_node 
                    new_node.parent = current 
                    break 
                else:
                    queue.append(current.right)

        self._heapify_up(new_node)

    def _heapify_up(self,node):
        while node.parent and node.value < node.parent.value:
            node.value, node.parent.value = node.parent.value,node.value 
            node = node.parent 
    
    
    def extract_min(self):
        if self.size == 0:
            return None
        
        min_value = self.root.value 

        if self.size == 1:
            self.root = None 
        
        else:
            last_node = self._get_last_node()
            self.root.value = last_node.value 

            if last_node.parent.left == last_node:
                last_node.parent.left = None 
            else:
                last_node.parent.right = None 

        self._heapify_down(self.root)

        return min_value
    
    def _heapify_down(self,node):
        smallest = node
        left = node.left 
        right = node.right 

        if left and left.value < smallest.value:
            smallest = left 
        
        if right and right.value < smallest.value:
            smallest = right 
        
        if smallest != node:
            node.value, smallest.value = smallest.value, node.value 
            self._heapify_down(smallest)

        
    def _get_last_node(self):
        queue = [self.root] 
        last_node = Node 

        while queue:
            current = queue.pop(0)
            last_node = current 
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
        return last_node 
    
    def print_heap(self):
        if self.root is None:
            print("Heap is empty")
        else:
            self._print_tree(self.root)
    
    def _print_tree(self, node, level=0):
        if node:
            self._print_tree(node.right,level + 1)
            print(" " * (level * 4) + str(node.value))
            self._print_tree(node.left, level + 1)

min_heap = MinHeap()

min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(5)
min_heap.insert(15)

min_heap.print_heap()

print("Extract Min:", min_heap.extract_min())  # Output: 5
min_heap.print_heap()

min_heap.insert(3)
min_heap.print_heap()

# Extract the minimum element again
print("Extract Min:", min_heap.extract_min())  # Output: 3
min_heap.print_heap()
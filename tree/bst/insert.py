class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

class BTS:
    def __init__(self):
        self.root = None 
    
    def insert(self, value):
        def _insert(node, value):
            if not node:
                return Node(value) 
            if value < node.value:
                node.left = _insert(node.left,value)
            else:
                node.right = _insert(node.right,value)
            
            return node 
        
        self.root = _insert(self.root, value) 

    
    def search(self,value):
        def _search(node, value):
            if not node:
                return 'Item not found'
            
            if value == node.value:
                return "value exist"
            elif value < node.value:
                return _search(node.left,value)
            else:
                return _search(node.right,value)
            
        return _search(self.root,value)
    
    def inorder(self):
        def _inorder(node):
            return _inorder(node.left) + [node.value] + _inorder(node.right) if node else []
        return _inorder(self.root)
    
    def preorder(self):
        def _preorder(node):
            return [node.value] + _preorder(node.left) + _preorder(node.right) if node else []
        return _preorder(self.root)


    def postorder(self):
        def _postorder(node):
            return _postorder(node.left) + _postorder(node.right) + [node.value] if node else []
        return _postorder(self.root)
    

tree = BTS()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

print("Inorder Traversal:", tree.inorder())
print("Preorder Traversal:", tree.preorder())
print("Postorder Traversal:", tree.postorder())
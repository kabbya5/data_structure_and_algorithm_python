## 🌳 Binary Search Tree (BST)

A **Binary Search Tree (BST)** is a type of **Binary Tree** where each node is arranged in such a way that:

- The value of every node in the **left subtree** is **less than** the current node.
- The value of every node in the **right subtree** is **greater than** the current node.

This structure makes operations like:

- 🔍 **Search**
- ➕ **Insert**
- ❌ **Delete**

very efficient — especially when working with **sorted data**.

---

## ✅ Advantages of BST

- 🔹 Efficient searching: Average time complexity is **O(log n)** for balanced trees.
- 🔹 Inorder traversal gives data in **sorted order**.
- 🔹 Dynamic structure: easy to insert/delete nodes without resizing like arrays.
- 🔹 Can be used to implement other data structures like **Sets**, **Maps**, etc.

---

## ❌ Disadvantages of BST

- 🔸 Performance degrades to **O(n)** if the tree becomes **unbalanced**.
- 🔸 Does **not handle duplicates** by default (requires custom logic).
- 🔸 Needs **self-balancing** (like AVL, Red-Black Trees) for guaranteed performance.

---
## 🧠 Use Cases

- 🗃️ **Databases** for indexing
- 🧮 **Auto-suggestion / auto-complete** systems
- 🔤 **Sorted data storage** and lookup
- 🛠️ **Compiler design** (symbol tables)
- 📊 Used in **search engines** and **memory management**

  ---

## 💻 Python Code Example

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

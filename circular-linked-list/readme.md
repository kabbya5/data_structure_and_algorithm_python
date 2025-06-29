## 🔁 What is a Circular Singly Linked List?

A **Circular Singly Linked List (CSLL)** is a type of linked 
list where the last node points 
back to the **first node**, forming a circle.
Unlike a regular singly linked list that ends with `null`, a CSLL **loops back**
to the beginning. This makes it useful for applications that require **circular traversal** 
(e.g., round-robin scheduling, buffering systems).


### ✅ Key Characteristics:

- Each node points to the **next node**.
- The **last node** points to the **first node**, not `null`.
- No `null` at the end of the list.
- Can be traversed infinitely in a circular way.

### 📌 Example Diagram:

[1] -> [2] -> [3] -> [4]
^_____________________|

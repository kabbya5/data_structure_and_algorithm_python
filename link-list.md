A linked list is a linear data structure in which elements, called nodes, are connected using pointers. Each node in a linked list contains:
![Alt text](https://miro.medium.com/v2/resize:fit:640/format:webp/1*MPEJnhLiRJ5vB3-Fp-Yjow.jpeg)
Time Complexcity:
Append:
Array: O(1) if there's space in a dynamic array  However, if the array needs doubling the capacity), this operation becomes O(n).
Singly Linked List: O(n) if we don’t have a tail pointer since we must traverse to the end. With a tail pointer, it’s O(1).
Prepend:
Array: O(n) because shifting all elements one position to the right is necessary to make room at the beginning.
Singly or Doubly Linked List: O(1) as we simply create a new node and adjust the head pointer to the new node.
pop:
Array: O(1) as no shifting is needed, just resizing the array if it's a dynamic array.
Singly Linked List: O(n) because we need to traverse to the second-to-last node to remove the last node.

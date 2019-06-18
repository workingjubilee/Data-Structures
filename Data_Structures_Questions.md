Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

O(1) in essentially every queue that doesn't seriously mess things up.

2. What is the runtime complexity of `dequeue`?

O(1) in an optimized queue. O(n) if we use an array.

3. What is the runtime complexity of `len`?

O(1) in an optimized queue. O(n) if we use a list that does not track its length.

## Binary Search Tree

1. What is the runtime complexity of `insert`?

O(log(n)) if the tree is reasonably optimized, which may require rotations to achieve. In this basic binary search tree with no rotations, it is possible for a theoretical configuration to assume O(n) complexity, but even with this poorly optimized version that is statistically unlikely if we are inserting random data. It becomes very likely if we are pushing in well-sorted data.

2. What is the runtime complexity of `contains`?

O(log(n)) with the same caveat.

3. What is the runtime complexity of `get_max`? 

O(log(n)) with the same caveat.

## Heap

1. What is the runtime complexity of `_bubble_up`?

O(log(n)).

2. What is the runtime complexity of `_sift_down`?

O(log(n)).

3. What is the runtime complexity of `insert`?

O(log(n)) in most configurations.

4. What is the runtime complexity of `delete`?

O(1) to get the topmost value, and then it becomes O(log(n)) to reconfigure the tree, so it will be O(log(n)).

5. What is the runtime complexity of `get_max`?

O(1).

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

...

10. What is the runtime complexity of `DoublyLinkedList.delete`?

O(1) for all of these, except that if you want to get a specific value from the middle of the list, like performing an array operation, or insert after a given item, then it's O(n), though the Ө will be Өn/2. Operations like DoublyLinkedList.delete are O(1) because they assume the user has a reference back to that node, which increases the space complexity. Just from the head or tail, though, is O(1), because in a DLL we are always going to track that anyways.

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

  The Array splice method has a much poorer runtime complexity.
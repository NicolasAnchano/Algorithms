# Algorithms

Recopilation of Data Structures and Algorithms, including a Linked List, trees and pipelines.


### Linked List

It's a linear data structure where elements are not stored in contiguous locations in memory, but rather have pointers for the previous (if any) and next (if any) elements.

It's faster than a typical array for inserting new elements, given you only have to look only at the index and the pointers (O(1) complexity for inserting, vs O(n) on an array) but slower for searching, as we have to scan every element from the first (O(n) complexity, vs O(1) on an array).


### Binary Tree

They are made by nodes, an abstract data types that contains references to the left and right nodes (they can even be None, as long as they contain a left and right reference). The top node is called root. A Node may have at most two children.

If a Node has a parent and at least one child, it's an Interior Node. These tell us the depth/height/levels of the tree.

We can traverse the tree in three ways:
	
   1. Preorder Traversal: Handle the value of the current node, then recursively traverse all the values on the left, and then on the right.
	
   2. Inorder Traversal: Recursively traverse all the values on the left, handle the value of the current node, and then recursively traverse the values on the right.
	
   3. Postorder Traversal: Recursively traverse all the values on the left, then on the right, then handle the value of the node.

![preorder_traverse](https://user-images.githubusercontent.com/63423173/97769300-731e8380-1b08-11eb-9746-14e4dc5a3c01.png)

Types of classification:

   1. Balanced/Unbalanced: A tree is balanced if the subtree's height does not differ in more than one, otherwise it's unbalanced.
	
   2. Complete/Incomplete: If each level of the tree, minus the last, is filled, it's complete. Otherwise it's incomplete.

![balanced_unbalanced_tree](https://user-images.githubusercontent.com/63423173/97769320-921d1580-1b08-11eb-8d5a-d2589b8aefbb.png)
![complete_noncomplete_tree](https://user-images.githubusercontent.com/63423173/97769324-9fd29b00-1b08-11eb-9f99-d876abe4ffa1.png)


### Heap Map (Binary Heap Tree)

A Binary Heap Tree is a binary tree where the values of a parent node is always higher/equal (Max heap, >=) or lower/equal (Min heap) than its childs.

![min_heap](https://user-images.githubusercontent.com/63423173/97769327-ad882080-1b08-11eb-9f7f-0da27e353245.png)
![max_heap](https://user-images.githubusercontent.com/63423173/97769333-bda00000-1b08-11eb-9680-cec8a5207bb0.png)


### Binary Search Tree (BST)

They are trees where every value in a node's left subtree is less than or equal to the parent; and every value to the right is more than or equal to the parent. Every node is inserted following these rules. So, if we do an inorder traversal, each node will be outputted in increased order.

![binary_search_tree](https://user-images.githubusercontent.com/63423173/97769361-ed4f0800-1b08-11eb-85c8-b4180e2c61b5.png)

Searching in the BST is fast. If it's balanced, then the deepest level we have to search is O(log(n)), like a binary search on a sorted list.

If the BST stays balanced after every insert, we call it a self balancing BST. We implemented that to speed up the search (if it's not balanced the search would be O(n), with n being the depth of the tree).


### B-Tree

It's a sorted and balanced tree that contains nodes with multiple keys and children (as in arrays), which helps us increase the speed at which we can query data. That is, every nodes will have more keys and references than the previous trees.

![b_tree](https://user-images.githubusercontent.com/63423173/97769366-fe981480-1b08-11eb-836b-75a239895f5d.png)

An index is a data structure with a key and a reference to a row of data. In an unsorted table, if we are searching for a row, without an index, we would have to iterate through the entire table (O(n) where n are the rows). Instead, with the index, if we knew that row was in some number, like 150, it would be a O(1) operation.

The degree (t) of the tree determines the minimum and maximum of the number of keys (with the exception of roots): t-1 and 2t-1 respectively. So, the degree t, is the minimum number of children a node can have. a B-Tree needs a minimum of t>=2, otherwise it would be a standard BST with one key and max of two children.

Searching or inserting in a B-Tree has O(m(n)) complexity, with m being the number of branches and n the number of keys. Inserting is time consuming, as it takes O(nlog(n)) because every value on insert takes O(log(n)) and we are inserting n values. It's recommended to save the data after inserting something like a csv on a pickle file or anything like that.


### Pipeline

Structures that perform a series of tasks. For this, they take iterables. For pipelines in particular, the concept of file streaming is important: break a file in small sections (chunks) and load each chunk into memory. When one is done, python loads the next one into memory to be iterated on.

A generator is an iterable object generated from a function, either by returning a tuple or using the keyword yield (on a for loop, for example).

With a Pipeline class, and a task method, we can dynamically change the behavior of the functions in terms of which inputs they take, that is, by which previous functions they depend on.

The basic pipeline is just a linear version, while the DAG one allows for multi-dependencies: executing two functions that depend on the same output. We achieve that by creating a dictionary of function: output. DAG below:

![dag](https://user-images.githubusercontent.com/63423173/97769377-17082f00-1b09-11eb-83f9-a02449d317da.png)

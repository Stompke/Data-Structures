"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue_for_bst import Queue
from stack_for_bst import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        if not self.value:
            self.__init__(value)
        elif value < self.value:
            # Go Left
            if not self.left:
                self.left = new_node
            else:
                self.left.insert(value)
                
        else:
            # Go Right
            if not self.right:
                self.right = new_node
            else:
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # self will be the root we start on
        #compare the target against self
        if target == self.value:
            return True
        if target < self.value:
            # go left
            # if there are no more nodes return False
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right
            # if there are no more nodes return False
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value
        if self.right:
            max_value = self.right.get_max()
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # pass
        # Create Queue
        queue = Queue()
        # enquque current node to queue
        queue.enqueue(node)
        while queue.__len__() > 0:
            current_working_node = queue.dequeue()
            print(current_working_node.value)
            if current_working_node.left:
                # add current_node.left to queue
                queue.enqueue(current_working_node.left)
                # print('current_node.left')
            if current_working_node.right:
                # add current_node.right to queue
                queue.enqueue(current_working_node.right)
                # print('current_node.right')
            



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # pass
        # Create Queue
        stack = Stack()
        # enquque current node to queue
        stack.push(node)
        while stack.__len__() > 0:
            current = stack.pop()
            if current.right:
                stack.push(current.right)
            if current.left:
                stack.push(current.left)
            
            print(current.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value)
        if node.left:
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)



    # Print Post-order recursive DFT
    def post_order_dft(self, node):

        if node.left:
            node.left.post_order_dft(node.left)
        if node.right:
            node.right.post_order_dft(node.right)
        print(node.value)


# my_bst = BSTNode(5)
# my_arr = []
# cb = lambda x: my_arr.append(x)



# my_bst.for_each(cb)
# print(my_arr)
# new_queue = Queue()

# print("length:", new_queue.__len__())
# new_queue.enqueue(BSTNode(1))
# print("length:", new_queue.__len__())
# new_queue.enqueue(BSTNode(5))
# print("length:", new_queue.__len__())
# new_queue.enqueue(BSTNode(3))
# print("length:", new_queue.__len__())
# new_queue.enqueue(BSTNode(12))
# print("length:", new_queue.__len__())
# print(new_queue.dequeue().value)
# print(new_queue.dequeue().value)
# print(new_queue.dequeue().value)
# print(new_queue.dequeue().value)
# print("length:", new_queue.__len__())

    # Building the Binary Search Tree
my_bst = BSTNode(1)
my_bst.insert(8)
my_bst.insert(5)
my_bst.insert(7)
my_bst.insert(6)
my_bst.insert(3)
my_bst.insert(4)
my_bst.insert(2)

    # Recursive Depth First Traversal
print('\n\t ***Recursive Depth First Traversal***')
my_bst.in_order_print(my_bst)

    # Iterative Breadth First Traversal 
print('\n\t ***Iterative Breadth First Traversal***')
my_bst.bft_print(my_bst)

    # Iterative depth first traversal
print('\n\t ***Iterative depth first traversal***')
my_bst.dft_print(my_bst)

    # Pre-order recursive DFT
print('\n\t ***Pre-order recursive DFT***')
my_bst.pre_order_dft(my_bst)

    # Post-order recursive DFT
print('\n\t ***Post-order recursive DFT***')
my_bst.post_order_dft(my_bst)


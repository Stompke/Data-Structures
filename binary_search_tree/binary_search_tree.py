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
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# my_bst = BSTNode(5)
# my_arr = []
# cb = lambda x: my_arr.append(x + 10)


# my_bst.insert(2)
# # print(my_bst.left.value)
# my_bst.insert(3)
# # print(my_bst.right.value)
# my_bst.insert(7)
# # print(my_bst.left.value)
# my_bst.insert(6)

# my_bst.for_each(cb)
# print(my_arr)


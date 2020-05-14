"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


### stack with Linked List storage structure
class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def remove_last(self):
        print(self.value)
    

class LinkedList:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        new_node = Node(value)
        # print(new_node.get_value())
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            # while current.get_next() is not None:
            #     current = current.get_next()
            self.head = new_node
            new_node.set_next(current)
            # current.set_next(new_node)

    def pop(self):
        # if list is 2 or more
        if self.head.get_next() is not None:
            current = self.head
            while current.get_next().get_next() is not None:
                current = current.get_next()
            removed = current.get_next().value
            current.set_next(None)
            # print("dequeue: ", removed) 
            return removed
        # if list is only 1
        if self.head is not None:
            current = self.head.get_value()
            self.head = None
            # print("dequeue: ", current)
            return current
            
            

    def len(self):
        if self.head is not None:
            count = 1
            current = self.head
            while current.get_next() is not None:
                count += 1
                current = current.get_next()
            return count
        else:
            return 0




class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.storage.len()

    def enqueue(self, value):
        self.storage.enqueue(value)

    def dequeue(self):
        if self.__len__():
            return self.storage.pop()


# new_queue = Queue()

# print("length:", new_queue.__len__())
# new_queue.enqueue(2)
# print("length:", new_queue.__len__())
# new_queue.enqueue(4)
# print("length:", new_queue.__len__())
# new_queue.enqueue(6)
# print("length:", new_queue.__len__())
# new_queue.enqueue(8)
# print("length:", new_queue.__len__())
# new_queue.dequeue()
# print("length:", new_queue.__len__())

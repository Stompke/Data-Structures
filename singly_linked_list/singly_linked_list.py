class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node
  def get_value(self):
    return self.value



  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
    def __init__(self):
        # first node in the list 
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node 
        new_node = Node(value)

        # what if the list is empty? 
        if not self.head:
            self.head = new_node
            self.tail = new_node
            print('add to tail: ', new_node.get_value())
            print('head value: ', self.head.value)
            print('tail value: ', self.tail.value)
        # what if the list isn't empty?
        else:
            # what node do we want to add the new node to? 
            # the last node in the list 
            # we can get to the last node in the list by traversing it 
            current = self.head 
            if current.get_next() is not None:
                while current.get_next() is not None:
                    current = current.get_next()
                # we're at the end of the linked list 
                current.set_next(new_node)
                self.tail = new_node
                print('add to tail: ', new_node.get_value())
                print('head value: ', self.head.value)
                print('tail value: ', self.tail.value)
            else:
                current.set_next(new_node) 
                self.tail = new_node
                print('add to tail: ', new_node.get_value())
                print('head value: ', self.head.value)
                print('tail value: ', self.tail.value)

    def remove_head(self):
        
        # what if the list is empty?
        if not self.head:
            print('No head to remove')
            return None
        # what if it isn't empty?
        elif self.head.get_next() is None:
            print('Remove Head', self.head.value)
            # we want to return the value at the current head 
            value = self.head.get_value()
            # remove the value at the head 
            # update self.head 
            self.head = None
            self.tail = None

            return value
        else:
            print('Remove Head', self.head.get_value())
            # we want to return the value at the current head 
            value = self.head.get_value()
            # remove the value at the head 
            # update self.head 
            if self.head.get_next() is not None:
                self.head = self.head.get_next()
                print('head value: ', self.head.value)
                print('tail value: ', self.tail.value)
            else:
                self.head = self.head.get_next()
                self.tail = self.head.get_next()
                print('head value: ', self.head.value)
                print('tail value: ', self.tail.value)

            return value

    def get_max(self):

        current = self.head
        max_num = current
        if not self.head:
            # print('stoppped here')
            return None
        # else:
        #     print(current.get_value())
        #     print(current.get_next().get_value())
        #     print(max_num.get_value())

        else:
            while current.get_next() is not None:
                if max_num.get_value() < current.get_next().get_value():
                    max_num = current.get_next()
                current = current.get_next()
            return max_num.get_value()
    def contains(self, num):
        current = self.head
        if self.head is not None:
            if self.head.value == num:
                return True
            else:
                while current.get_next() is not None:
                    if current.get_next().get_value() == num:
                        return True
                    current = current.get_next()

                return False
        else:
            return False
            
# my_list = LinkedList()
# my_list.add_to_tail(3)
# print('head value: ', my_list.head.value)
# print('tail value: ', my_list.tail.value)
# my_list.add_to_tail(6)
# print('head value: ', my_list.head.value)
# print('tail value: ', my_list.tail.value)

# print(my_list.get_max())

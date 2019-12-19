import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    # always takes the last one that was put in
    # like a bizarro line where the last person gets served first

    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        val = self.storage.remove_from_tail()        
        if val:
            self.size -= 1
            return val

    def len(self):
        # pass
        return self.size
        # return len(self.storage)


stack = Stack()

print(stack.storage)
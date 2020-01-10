import math
"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
      return str(self.value)

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            # deleting tail: change the next of the new tail 
            # to null
            self.prev.next = self.next
            # deleting head: prev of new head will be null.
            # wipes out the connection to the old head
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def print(self):
      curr_node = self.head
      print(curr_node)
      while curr_node.next is not None:
        curr_node = curr_node.next
        print(curr_node)

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    # unshift
    def add_to_head(self, value):
      new_node = ListNode(value)  

      # using length here cuz i like it better
      if self.length == 0:
        self.head = new_node
        self.tail = new_node
      else:
        # making the new node the head
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node  
      self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    # shift.
    def remove_from_head(self):
        if self.head == None:
          return
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    # push
    def add_to_tail(self, value):
      new_node = ListNode(value) 
      self.length += 1
      if not self.head and not self.tail:
        self.head = new_node
        self.tail = new_node
      else:
        # making new node the tail
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    # why wasnt this just named pop?
    def remove_from_tail(self):

        if self.tail == None:
          return
        # cant get the value of something that doesnt exist.
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
          return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
          return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail:
          return
        if self.head == self.tail:
          self.head = None
          self.tail = None
          self.length -=1
        elif self.head == node:
          # new head is the node after current head
          self.head = node.next
          self.length -= 1
          node.delete()
        elif self.tail == node:
          # new tail is the node before the current tail.
          self.tail = node.prev
          self.length -= 1
          # handles the ties around this specific node
          node.delete()
        else:
          self.length -= 1
          node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
      maxVal = -math.inf
      current = self.head

      if not current:
        return 'no values in list'

      while current:
        if current.value > maxVal:
          maxVal = current.value

        current = current.next

      return maxVal

doubly = DoublyLinkedList()

doubly.add_to_tail(7)
doubly.add_to_tail(6)
# print(doubly.get_max())
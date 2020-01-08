import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self, value):
    # like the root
    self.value = value
    self.left = None
    self.right = None

  # Insert the given value into the tree
  def insert(self, value):
    newNode = Node(value)
    current = self

    while True:
      if newNode.value > current.value:
        if current.right:
          current = current.right
        else:
          current.right = newNode
          break
      elif newNode.value < current.value:
        if current.left:
          current = current.left
        else:
          current.left = newNode
          break


  # Return True if the tree contains the value
  # False if it does not
  def contains(self, target):
    current = self

    while True:
      if target == current.value:
        return True
      elif target > current.value:
        if current.right:
          current = current.right
        else:
          return False
      elif target < current.value:      
        if current.left:
          current = current.left
        else:
          return False                  

  # Return the maximum value found in the tree
  def get_max(self):
    current = self

    while True:
      if current.right:
        current = current.right
      else:
        break

    return current.value

  # Call the function `cb` on the value of each node
  # You may use a recursive or iterative approach
  def for_each(self, cb):
    queue = Queue()

    queue.enqueue(self)

    while queue.len() > 0:
      current = queue.dequeue()
      # need to call func on the value of the node
      cb(current.value)

      if current.left:
        queue.enqueue(current.left)
      if current.right:
        queue.enqueue(current.right)

  # DAY 2 Project -----------------------

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

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
    pass

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
    pass

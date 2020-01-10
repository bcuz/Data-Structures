import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

# class Node:
#   def __init__(self, value):
#     self.value = value
#     self.left = None
#     self.right = None

class BinarySearchTree:
  def __init__(self, value):
    # like the root
    self.value = value
    self.left = None
    self.right = None

  # Insert the given value into the tree
  def insert(self, value):
    # newNode = Node(value)
    current = self

    if value > current.value:
      if current.right:
        current.right.insert(value)
      else:
        current.right = BinarySearchTree(value)
    elif value < current.value:
      if current.left:
        current.left.insert(value)
      else:
        current.left = BinarySearchTree(value)

    # def recursion(current):
    #   if newNode.value > current.value:
    #     if current.right:
    #       current = current.right
    #       recursion(current)
    #     else:
    #       current.right = newNode          
    #   elif newNode.value < current.value:
    #     if current.left:
    #       current = current.left
    #       recursion(current)
    #     else:
    #       current.left = newNode          
    # recursion(current)    

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

    if node.left:
      self.in_order_print(node.left)
    print(node.value)
    if node.right:
      self.in_order_print(node.right)


  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(self, node):
    queue = Queue()

    queue.enqueue(node)

    while queue.len() > 0:
      current = queue.dequeue()
      # need to call func on the value of the node
      print(current.value)

      if current.left:
        queue.enqueue(current.left)
      if current.right:
        queue.enqueue(current.right)

  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(self, node):
    stack = Stack()
    stack.push(node)

    while stack.len() > 0:
      current = stack.pop()
      print(current.value)

      if current.right:
        stack.push(current.right)
      if current.left:
        stack.push(current.left)

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
    print(node.value)
    if node.left:
      self.pre_order_dft(node.left)
    if node.right:
      self.pre_order_dft(node.right)

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
    if node.left:
      self.post_order_dft(node.left)
    if node.right:
      self.post_order_dft(node.right)
    print(node.value)

bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)

#    5
# 2    7
#  3

bst.post_order_dft(bst)
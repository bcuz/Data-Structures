# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    # dll has all the keys in the order they have to be. can at least
    # try that first
    # storage dict has both keys and values
    def __init__(self, limit=10):
        self.limit = limit
        self.current = 0
        self.dll = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    # moving to tail.
    def get(self, key):
        # how do i retrieve the specific node i need?
        # might need to write a get for the DLL. get by value

        if key not in self.storage:
            return None

        # each key holds a node
        node = self.storage[key]

        # str func of dll file was making things more confusing.
        # print(node.value)

        self.dll.move_to_end(node)
        return node.value[1]

        # if node:
        #     self.dll.move_to_end(node)
        #     return node.value[1]
        # else:
        #     return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if specific key already there, we only update it's value
        if key in self.storage:
            node = self.storage[key]

            node.value = (key, value)

            return

        # if already at limit, remove the oldest item
        if self.current == self.limit:
            val = self.dll.remove_from_head()
            
            del self.storage[val[0]]
            self.current -= 1

        # add the new item
        # value is a tuple
        self.dll.add_to_tail((key,value))
        # storing the node itself in the dict
        self.storage[key] = self.dll.tail
        self.current += 1

lru = LRUCache(1)
lru.set('hi', 5)
# lru.set('hi', 6)
lru.get('hi')
# print(lru.storage['hi'])
# lru.get('hi')
# doubly = DoublyLinkedList()

# doubly.add_to_tail(7)
# print(doubly.length)
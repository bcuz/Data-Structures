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

        # this will be none if no item found
        node = self.dll.get(key)

        if node:
            self.dll.move_to_end(node)
            return self.storage[node.value]
        else:
            return None

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
            self.storage[key] = value
            return

        # if already at limit, remove the oldest item
        if self.current == self.limit:
            val = self.dll.remove_from_head()
            del self.storage[val]
            self.current -= 1

        # add the new item
        self.storage[key] = value
        self.dll.add_to_tail(key)
        self.current += 1

lru = LRUCache(1)
# lru.set('hi', 5)
# lru.set('bye', 6)
print(lru.get('nothere'))
# print(lru.dll.tail)
# lru.get('hi')
# doubly = DoublyLinkedList()

# doubly.add_to_tail(7)
# print(doubly.length)
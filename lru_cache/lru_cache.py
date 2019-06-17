from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.list = DoublyLinkedList()
        self.dict = {}

    """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """

    def get(self, key):
        catch = self.dict.get(key)
        if catch != None:
            self.list.move_to_front(catch)
            return catch.value
        else:
            return catch
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
        node = self.list.add_to_head(value)

        if self.dict.get(key) == None:
            self.dict[key] = node
            if self.list.length > self.limit:
                for k, v in self.dict.items():
                    if v == self.list.tail:
                        del self.dict[k]
                        self.list.remove_from_tail()
                        break
        else:
            self.dict[key].delete()
            self.dict[key] = node
            self.list.length -= 1

        return node

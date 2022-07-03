# LRU cache
class Node:
   def __init__(self, key, value, next, prev):
    self.key = key
    self.next = next #default would pass None
    self.prev = prev
    self.value = value


class Cache:
  def __init__(self, size):
    self.max_size = size
    self.map = {}
    self.head = None
    self.tail = None

  def add(self, key, value):
    if self.map[key] is not None:
      self.map[key].value = value
      prev = self.map[key].prev
      next = self.map[key].next
      prev.next = next
      next.prev = prev
      # take the node to be first in line
      second = self.head
      first = self.map[key]
      first.next = second
      second.prev = first
      self.head = first
    else:
      if self.max_size == len(self.map):
        self.map.remove(self.tail.key)
        self.tail.prev.next = None
        self.map[key] = Node(key, value, None, None)
        self.map[key].next = self.head
        self.head = self.map[key]
        self.head.next.prev = self.head
      else:
        if self.head is None:
          self.map[key] = self.head = self.tail = Node(key, value, None, None)
        else:
          second = self.head
          first = Node(key, value, None, None)
          first.next = second
          second.prev = first
          self.head = first
          self.map[key] = first

  def get(self, key):
    if self.map[key] is None:
      return None

    # make the node first in line
    if self.map[key] is self.head:
      return self.map[key].value
    if self.map[key] is self.tail:
      self.tail.prev.next = None
      self.tail = self.tail.prev
      # move to the first position
      second = self.head
      first = self.map[key]
      self.head = first
      first.next = second
      second.prev = first

    prev = self.map[key].prev
    next = self.map[key].next
    prev.next = next
    next.prev = prev
    # take the node to be first in line
    second = self.head
    first = self.map[key]
    first.next = second
    second.prev = first
    self.head = first

    return self.map[key].value

class Stack:
    def __init__(self):
      self._items = []

    def push(self, item):
      self._items.append(item)

    def pop(self, item):
      if self.get_size() > 0:
        return self._items.pop()
      else:
        raise LookupError("stack of size 0 can not be popped")

    def peek(self):
      return self._items[-1]

    def get_size(self):
      return len(self._items)

from collections import deque 

class Queue:
    def __init__(self):
      self._queue = deque([])

    def push(self, item):
      self._queue.append(item)

    def pop(self):
      if self.get_size() > 0:
        return self._queue.popleft()
      else:
        raise LookupError("stack of size 0 can not be popped")

    def peek(self):
      return self._queue[0]

    def get_size(self):
      return len(self._queue)

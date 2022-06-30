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

print("queue test")
queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
print(f"peek first {queue.pop()}")
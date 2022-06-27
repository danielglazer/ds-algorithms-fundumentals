class SinglyLinkedListNode:
  def __init__(self, data, next) -> None:
    self.data = data
    self.next = next

class SinglyLinkedList:
  def __init__(self) -> None:
    self.head = self.tail = None
  
  def add_node(self, node: SinglyLinkedListNode):
    if self.head == None:
      self.head = node
    self.tail.next = node
    self.tail = node

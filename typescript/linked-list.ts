class ListNode<T> {
  constructor(
    public data: T,
    public next: ListNode<T> | null = null,
    public prev: ListNode<T> | null = null,
    ) {}
}

class LinkedList<T> {
  head: ListNode<T> | null;
  tail: ListNode<T> | null;
  size: number;
  constructor() {
    this.head = this.tail = null;
    this.size = 0;
  }
}
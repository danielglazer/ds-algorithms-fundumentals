class Stack<T> {
  constructor(private items: T[] = []){}

  push(item: T) {
    this.items.push(item);
  }

  pop(): T {
    return this.items.pop();
  }

  peek(): T {
    if(this.items.length > 0){
      return this.items[-1];
    }
  }
}
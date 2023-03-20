interface IQueue<T> {
  queue: (T | undefined)[];
  length: number;
  head: number;
  tail: number;

  push(element: T): void;
  popLeft(): T;
  isFull(): boolean;
  isEmpty(): boolean;
  show(): void;
}

class Queue<T> implements IQueue<T> {
  queue: (T | undefined)[];
  length: number;
  head: number;
  tail: number;

  constructor(length: number) {
    this.queue = new Array(length).fill(undefined);
    this.length = length;
    this.head = 0;
    this.tail = 0;
  }

  push(element: T) {
    if (this.isFull()) throw new Error('queue is full!');
    this.queue[this.tail] = element;
    this.tail = (this.tail + 1) % this.length;
  }

  popLeft(): T {
    if (this.isEmpty()) throw new Error('queue is empty!');
    const value: T = this.queue[this.head]!;
    this.queue[this.head] = undefined;
    this.head = (this.head + 1) % this.length;
    return value;
  }

  isFull(): boolean {
    return this.head === this.tail && this.queue[this.tail] !== undefined;
  }

  isEmpty(): boolean {
    return this.queue[this.head] === undefined;
  }

  show() {
    console.log(this.queue);
  }
}

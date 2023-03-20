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

// input
const input: string[] = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
const numOfVertex: number = Number(input[0]![0]);
const graph: { [key: number]: number[] } = {};
const visited: boolean[] = new Array(numOfVertex + 1).fill(false);
const queue = new Queue<number>(numOfVertex);
let res = 0;

for (let i = 1; i < input.length; i++) {
  const [left, right] = input[i]!.split(' ').map(Number);
  if (!graph[left!]) graph[left!] = [];
  if (!graph[right!]) graph[right!] = [];
  graph[left!]!.push(right!);
  graph[right!]!.push(left!);
}

// solution
const bfs = (startNode: number) => {
  visited[startNode] = true;

  if (graph[startNode]) {
    graph[startNode]!.forEach((node) => {
      if (!visited[node]) {
        queue.push(node);
      }
    });
  }

  while (!queue.isEmpty()) {
    const nextNode = queue.popLeft();
    visited[nextNode] = true;
    graph[nextNode]!.forEach((node) => {
      if (!visited[node]) {
        queue.push(node);
      }
    });
  }
};

for (let node = 1; node <= numOfVertex; node++) {
  if (!visited[node]) {
    res++;
    bfs(node);
  }
}

// output
console.log(res);

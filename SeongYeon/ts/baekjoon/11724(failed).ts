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
let willVisit: number[] = new Array(numOfVertex);

let head = 0;
let tail = 0;
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
        willVisit[tail] = node;
        tail = (tail + 1) % numOfVertex;
      }
    });
  }

  while (head !== tail) {
    const nextNode: number = willVisit[head]!;
    head = (head + 1) % numOfVertex;
    visited[nextNode] = true;
    graph[nextNode]!.forEach((node) => {
      if (!visited[node]) {
        willVisit[tail] = node;
        tail = (tail + 1) % numOfVertex;
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

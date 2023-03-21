// input
const input: string[] = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .split('\n');

// variable
const [n, m] = input[0]!.split(' ').map(Number);
const edges: string[] = input.slice(1, 1 + m!);
const graph: number[][] = Array.from(Array(n! + 1), () => new Array());
const visited: boolean[] = Array(n! + 1).fill(false);
let answer: number = 0;

edges.forEach((row) => {
  const [a, b] = row.split(' ').map(Number);
  graph[a!]!.push(b!);
  graph[b!]!.push(a!);
});

// solution
const bfs = (startNode: number) => {
  const queue = [startNode];

  while (queue.length > 0) {
    const nextNode: number = queue.shift()!;

    graph[nextNode]!.forEach((node) => {
      if (!visited[node]) {
        visited[node] = true;
        queue.push(node);
      }
    });
  }
};

for (let i = 1; i <= n!; i++) {
  if (!visited[i]) {
    visited[i] = true;
    bfs(i);
    answer++;
  }
}

// output
console.log(answer);

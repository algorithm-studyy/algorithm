// input
const input: string[] = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
const [n, m] = input[0]!.split(' ').map(Number);
const maze: number[][] = Array.from(Array(n! + 2), () => Array(m! + 2).fill(0));
const visited: boolean[][] = Array.from(Array(n! + 2), () =>
  Array(m! + 2).fill(false)
);
const queue: number[][] = [];

for (let i = 1; i <= n!; i++) {
  maze[i] = [0, ...input[i]!.split('').map(Number), 0];
}

const dx: number[] = [0, 0, -1, 1];
const dy: number[] = [-1, 1, 0, 0];

// solution
const bfs = (x: number, y: number, distance: number) => {
  maze[x]![y] = distance;
  visited[x]![y] = true;
  for (let i = 0; i < 4; i++) {
    const nextX: number = x + dx[i]!;
    const nextY: number = y + dy[i]!;

    if (maze[nextX]![nextY] && !visited[nextX]![nextY])
      queue.push([nextX, nextY]);
  }

  while (queue.length !== 0) {
    for (let i = 0; i < queue.length; i++) {
      bfs(queue[i]![0]!, queue[i]![1]!, distance + 1);
      queue.shift();
    }
  }
};

bfs(1, 1, 1);

// output
console.log(maze);

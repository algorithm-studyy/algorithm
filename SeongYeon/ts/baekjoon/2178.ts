// input
const input: string[] = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .split('\n');

// variable
const [n, m] = input[0]!.split(' ').map(Number);
const map: number[][] = Array.from(input.slice(1, 1 + n!), (row) =>
  row.split('').map(Number)
);
const move: number[][] = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];

// solution
const bfs = (startX: number, startY: number) => {
  const queue: number[][] = [[startX, startY]];

  while (queue.length !== 0) {
    const [x, y] = queue.shift()!;

    move.forEach((xy) => {
      const nextX = x! + xy[0]!;
      const nextY = y! + xy[1]!;
      if (nextX < 0 || nextX >= n! || nextY < 0 || nextY >= m!) return;
      if (nextX === 0 && nextY === 0) return;

      if (map[nextX]![nextY]! === 1) {
        queue.push([nextX, nextY]);
        map[nextX]![nextY] = map[x!]![y!]! + 1;
      }
    });
  }
};

bfs(0, 0);

// output
console.log(map[n! - 1]![m! - 1]);

// input
const input: string[] = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .split('\n');

// variable
const n: number = Number(input[0]!);
const map: string[][] = Array.from(input.slice(1, 1 + n), (row) =>
  row.split('')
);
const visited: boolean[][] = Array.from(Array(n), () =>
  new Array(n).fill(false)
);
const move: number[][] = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];
const groupCount: number[] = [];
let numOfGroup: number = 0;

// solution
const bfs = (startX: number, startY: number) => {
  const queue: number[][] = [[startX, startY]];

  while (queue.length !== 0) {
    const [x, y] = queue.shift()!;
    groupCount[numOfGroup]++;

    move.forEach((xy) => {
      const nextX = x! + xy[0]!;
      const nextY = y! + xy[1]!;
      if (nextX < 0 || nextX >= n || nextY < 0 || nextY >= n) return;
      if (map[nextX]![nextY] === '1' && !visited[nextX]![nextY]) {
        queue.push([nextX, nextY]);
        visited[nextX]![nextY] = true;
      }
    });
  }
};

map.forEach((row, i) => {
  row.forEach((item, j) => {
    if (item === '1' && !visited[i]![j]) {
      visited[i]![j] = true;
      groupCount[numOfGroup] = 0;
      bfs(i, j);
      numOfGroup++;
    }
  });
});

// output
const res: number[] = [numOfGroup, ...groupCount.sort((a, b) => a - b)];
console.log(res.join('\n'));

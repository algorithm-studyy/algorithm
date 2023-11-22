// input
const fs = require('fs');
const inputFile =
  process.platform === 'linux' ? '/dev/stdin' : 'test/input.txt';
const input = fs.readFileSync(inputFile).toString().split('\n');

// solution
const [N, M] = input[0].split(' ').map(Number);
const dir = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];
const queue = [];
const map = [];
const newMap = [];
let visited = [];

for (let i = 0; i < N; i++) {
  map[i] = input[i + 1].split(' ').map(Number);
  newMap[i] = input[i + 1].split(' ').map(Number);
}

let section;
let count = 0;

const bfs = (i, j) => {
  queue.push([i, j]);
  visited[i][j] = true;

  while (queue.length !== 0) {
    const [x, y] = queue.shift();

    dir.forEach((d) => {
      const dx = x + d[0];
      const dy = y + d[1];

      if (map[dx][dy] !== 0 && !visited[dx][dy]) {
        queue.push([dx, dy]);
        visited[dx][dy] = true;
      }
      if (map[dx][dy] === 0 && newMap[x][y] !== 0) newMap[x][y] -= 1;
    });
  }
};

do {
  visited = Array.from(Array(N), () => new Array(M));

  section = 0;
  count += 1;

  for (let i = 1; i < N - 1; i++) {
    for (let j = 1; j < M - 1; j++) {
      if (map[i][j] !== 0 && !visited[i][j]) {
        bfs(i, j);
        section += 1;
      }
    }
  }

  for (let row = 1; row < N - 1; row++) {
    map[row] = [...newMap[row]];
  }
} while (section === 1);

console.log(section ? count - 1 : 0);

/* input */
const fs = require('fs');
const inputFile =
  process.platform === 'linux' ? '/dev/stdin' : 'test/input.txt';
const input = fs.readFileSync(inputFile).toString().split('\n');

/* solution */
const n = Number(input[0]);
const moves = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];
const mapForNormal = [];
const mapForBlind = [];
let normal = 0;
let blind = 0;

for (let i = 0; i < n; i++) {
  mapForNormal[i] = input[i + 1].split('');
  mapForBlind[i] = input[i + 1].split('');
}

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (mapForBlind[i][j] === 'R') mapForBlind[i][j] = 'G';
  }
}

const bfs = (map) => {
  const visited = Array.from(Array(n), () => Array(n).fill(false));
  const queue = [];
  let res = 0;

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (visited[i][j]) continue;

      const pickedColor = map[i][j];
      queue.push([i, j]);
      visited[i][j] = true;

      while (queue.length !== 0) {
        const pos = queue.shift();

        for (const move of moves) {
          const dy = pos[0] + move[0];
          const dx = pos[1] + move[1];

          if (dy < 0 || dy >= n || dx < 0 || dx >= n || visited[dy][dx])
            continue;
          if (map[dy][dx] !== pickedColor) continue;
          queue.push([dy, dx]);
          visited[dy][dx] = true;
        }
      }
      res += 1;
    }
  }

  return res;
};

normal = bfs(mapForNormal);
blind = bfs(mapForBlind);

/* output */
console.log(`${normal} ${blind}`);

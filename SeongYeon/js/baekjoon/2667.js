// input
const fs = require('fs');
const inputFile =
  process.platform === 'linux' ? '/dev/stdin' : 'test/input.txt';
const input = fs.readFileSync(inputFile).toString().split('\n');

const map = [];
const length = Number(input[0]);
const visited = Array.from(Array(length), () => Array(length).fill(false));
for (let i = 1; i <= length; i++) map[i - 1] = input[i].split('');

// solution
let result = [];
const queue = [];
const goTo = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];

for (let i = 0; i < length; i++) {
  for (let j = 0; j < length; j++) {
    if (!visited[i][j] && map[i][j] === '1') {
      visited[i][j] = true;
      queue.push([i, j]);
      let count = 1;

      while (queue.length) {
        const loc = queue.shift();
        goTo.forEach((go) => {
          const dx = loc[0] + go[0];
          const dy = loc[1] + go[1];

          if (dx >= 0 && dx < length && dy >= 0 && dy < length)
            if (map[dx][dy] === '1' && !visited[dx][dy]) {
              visited[dx][dy] = true;
              queue.push([dx, dy]);
              count++;
            }
        });
      }

      result.push(count);
    }
  }
}

// output
console.log(result.length);
console.log(result.sort((a, b) => a - b).join('\n'));

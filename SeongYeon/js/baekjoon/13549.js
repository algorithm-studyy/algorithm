// input
const fs = require('fs');
const inputFile =
  process.platform === 'linux' ? '/dev/stdin' : 'test/input.txt';
const input = fs.readFileSync(inputFile).toString().split(' ');

// solution
const [N, K] = input.map(Number);
let distance = K - N;
let current = N;
let result = 0;

while (distance > 0) {
  if (current * 2 <= K) {
    current *= 2;
    distance = K - current;
    continue;
  }
  // ...?
}

return result - distance;

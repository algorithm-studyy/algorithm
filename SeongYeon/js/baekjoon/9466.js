// input
const fs = require('fs');
const inputFile =
  process.platform === 'linux' ? '/dev/stdin' : 'test/input.txt';
const input = fs.readFileSync(inputFile).toString().split('\n');

// solution
const solution = (N, nodeList) => {
  let result = N;
  const visited = new Array(N + 1).fill(false);
  const done = new Array(N + 1).fill(false);

  const dfs = (firstNode, currentNode, count) => {
    if (visited[currentNode]) {
      if (currentNode === firstNode) result -= count;
      else if (currentNode === nodeList[currentNode - 1]) result -= 1;

      visited.forEach((value, idx) => (done[idx] = done[idx] || value));
      return;
    }

    visited[currentNode] = true;
    if (!done[nodeList[currentNode - 1]]) {
      dfs(firstNode, nodeList[currentNode - 1], count + 1);
    }
    visited[currentNode] = false;
  };

  for (let i = 1; i <= N; i++) {
    if (done[i] || done[nodeList[i - 1]]) continue;

    visited[i] = true;
    dfs(i, nodeList[i - 1], 1);
    visited[i] = false;
  }

  console.log(result);
};

for (let i = 1; i < input.length; i += 2) {
  solution(Number(input[i]), input[i + 1].split(' ').map(Number));
}

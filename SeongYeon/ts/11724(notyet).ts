// input
const input: string[] = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : 'input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
const [n, m] = input[0]!.split(' ').map(Number);
const visited: boolean[] = new Array(n! + 1).fill(false);
const edge: { [key: number]: number[] } = {};
for (let i = 1; i <= m!; i++) {
  const [vertex1, vertex2] = input[i]!.split(' ').map(Number);
  edge[vertex1!] = [...(edge[vertex1!] || []), vertex2!];
  edge[vertex2!] = [...(edge[vertex2!] || []), vertex1!];
}

// solution
const bfs = () => {
  while (!visited.includes(false)) {}
};

// output
console.log(edge);

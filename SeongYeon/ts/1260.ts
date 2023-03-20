// input
const input: string[] = require('fs')
  .readFileSync(process.platform === 'linux' ? '/dev/stdin' : './input.txt')
  .toString()
  .trim()
  .split('\n');

// variable
const start: number = Number(input[0]!.split(' ')[2]);
const graph: { [key: number]: number[] } = {};
for (let i = 1; i < input.length; i++) {
  const [left, right] = input[i]!.split(' ').map(Number);
  graph[left!] = graph[left!] ? [...graph[left!]!, right!] : [right!];
  graph[right!] = graph[right!] ? [...graph[right!]!, left!] : [left!];
  graph[left!]!.sort((a, b) => a - b);
  graph[right!]!.sort((a, b) => a - b);
}

// solution
const dfs = (startNode: number) => {
  const visited: number[] = [];
  let willVisit: number[] = [];

  visited.push(startNode);
  willVisit = graph[startNode] ? [...graph[startNode]!] : [];

  while (willVisit.length) {
    const nextNode: number = willVisit.shift()!;
    if (!visited.includes(nextNode)) {
      visited.push(nextNode);
      willVisit = graph[nextNode!]
        ? [...graph[nextNode!]!, ...willVisit]
        : [...willVisit];
    }
  }

  console.log(visited.join(' '));
};

const bfs = (startNode: number) => {
  const visited: number[] = [];
  let willVisit: number[] = [];

  visited.push(startNode);
  willVisit = graph[startNode] ? [...graph[startNode]!] : [];

  while (willVisit.length) {
    const nextNode: number = willVisit.shift()!;
    if (!visited.includes(nextNode)) {
      visited.push(nextNode);
      willVisit = graph[nextNode!]
        ? [...willVisit, ...graph[nextNode!]!]
        : [...willVisit];
    }
  }

  console.log(visited.join(' '));
};

// output
dfs(start);
bfs(start);

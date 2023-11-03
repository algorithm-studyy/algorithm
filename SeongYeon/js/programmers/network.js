function solution(n, computers) {
  const connection = {};
  const visited = [];
  let queue = [];
  let answer = 0;

  for (let i in computers) {
    for (let j in computers[i]) {
      if (i === j || computers[i][j] === 0) continue;
      if (!connection[i]) connection[i] = [j];
      else connection[i].push(j);
    }
  }

  if (Object.keys(connection).length === 0) return n;

  for (let startNode = 0; startNode < n; startNode++) {
    if (!connection[startNode]) {
      answer += 1;
      continue;
    }

    if (!visited[startNode]) {
      answer += 1;
      visited[startNode] = true;
      queue = [...queue, ...connection[startNode]];

      while (queue.length !== 0) {
        const node = queue.shift();
        if (!visited[node]) {
          visited[node] = true;
          queue = [...queue, ...connection[node]];
        }
      }
    }
  }

  return answer;
}

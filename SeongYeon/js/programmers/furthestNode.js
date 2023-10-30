function solution(n, edge) {
  const visited = [];
  const edges = {};
  const queue = [[1, 0]];
  let maxDist = 0;
  let answer = 0;

  edge.forEach((e) => {
    edges[e[0]] = edges[e[0]] ? [...edges[e[0]], e[1]] : [e[1]];
    edges[e[1]] = edges[e[1]] ? [...edges[e[1]], e[0]] : [e[0]];
  });

  while (queue.length !== 0) {
    const [vertex, distance] = queue.shift();

    if (!visited[vertex]) {
      visited[vertex] = true;
      edges[vertex].forEach((v) => {
        if (!visited[v]) queue.push([v, distance + 1]);
      });

      if (distance > maxDist) {
        maxDist = distance;
        answer = 1;
      } else if (distance === maxDist) {
        answer += 1;
      }
    }
  }

  return answer;
}

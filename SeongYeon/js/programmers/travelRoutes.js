function solution(tickets) {
  const visited = [];
  let answer = [];

  tickets.sort(([start1, end1], [start2, end2]) => {
    if (start1 < start2) return -1;
    else if (start1 > start2) return 1;
    else {
      if (end1 < end2) return -1;
      else if (end1 > end2) return 1;
      return 0;
    }
  });

  const dfs = (idx, routes) => {
    if (answer.length !== 0) return;

    if (routes.length >= tickets.length) {
      answer = [...routes, tickets[idx][1]];
      return;
    }

    visited[idx] = true;
    for (let j = 0; j < tickets.length; j++) {
      if (!visited[j] && tickets[j][0] === tickets[idx][1]) {
        dfs(j, [...routes, tickets[j][0]]);
      }
    }
    visited[idx] = false;
  };

  for (let i = 0; i < tickets.length; i++) {
    if (tickets[i][0] === 'ICN') dfs(i, ['ICN']);
  }

  return answer;
}

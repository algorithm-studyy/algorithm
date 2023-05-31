function solution(n) {
  let answer = 0;
  let queens = [];

  const dfs = (x, y) => {
    if (queens.length === n) {
      answer++;
      return;
    }
    if (x === n) return;
    if (y === n) dfs(x + 1, 0);
    else {
      let isOk = true;
      for (let queen of queens) {
        if (
          queen[0] === x ||
          queen[1] === y ||
          Math.abs(x - queen[0]) === Math.abs(y - queen[1])
        ) {
          isOk = false;
          break;
        }
      }

      if (isOk) queens.push([x, y]);
      dfs(x, y + 1);
      if (isOk) queens.pop();
    }
  };
  //
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      dfs(i, j);
    }
  }

  return answer;
}

function solution(maps) {
  const n = maps.length;
  const m = maps[0].length;
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];
  const queue = [[0, 0]];

  while (queue.length !== 0) {
    const [x, y] = queue.shift();

    for (let i = 0; i < 4; i++) {
      const nextX = x + dx[i];
      const nextY = y + dy[i];

      if (nextX < 0 || nextX > n - 1) continue;
      if (nextY < 0 || nextY > m - 1) continue;
      if (nextX === 0 && nextY === 0) continue;
      if (maps[nextX][nextY] !== 1) continue;

      maps[nextX][nextY] += maps[x][y];
      queue.push([nextX, nextY]);
    }
  }

  if (maps[n - 1][m - 1] === 1) return -1;
  return maps[n - 1][m - 1];
}

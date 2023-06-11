function solution(maps) {
  const mapList = maps.map((row) => row.split(''));
  const direction = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];
  const nextVisit = [];
  const res = [];

  for (let i = 0; i < mapList.length; i++) {
    for (let j = 0; j < mapList[0].length; j++) {
      if (mapList[i][j] === 'X') continue;

      let count = 0;
      nextVisit.push([i, j]);

      while (nextVisit.length !== 0) {
        const [x, y] = nextVisit.shift();

        if (mapList[x][y] === 'X') continue;

        count += Number(mapList[x][y]);
        mapList[x][y] = 'X';

        direction.forEach(([dx, dy]) => {
          if (x + dx < 0 || x + dx >= mapList.length) return;
          if (y + dy < 0 || y + dy >= mapList[0].length) return;

          if (mapList[x + dx][y + dy] !== 'X') nextVisit.push([x + dx, y + dy]);
        });
      }
      res.push(count);
    }
  }

  if (res.length === 0) return [-1];
  return res.sort((a, b) => a - b);
}

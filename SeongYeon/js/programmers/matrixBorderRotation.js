function solution(rows, columns, queries) {
  const res = [];

  // 맵 생성
  const map = Array.from(new Array(rows + 1), () =>
    new Array(columns + 1).fill(0)
  );
  for (let x = 1; x <= rows; x++) {
    for (let y = 1; y <= columns; y++) {
      map[x][y] = (x - 1) * columns + y;
    }
  }

  // 회전
  queries.forEach((query) => {
    const [x1, y1, x2, y2] = query;
    const firstVal = map[x1][y1];
    let minVal = map[x1][y1];

    // 왼쪽
    for (let x = x1; x < x2; x++) {
      map[x][y1] = map[x + 1][y1];
      minVal = Math.min(minVal, map[x][y1]);
    }

    // 아래
    for (let y = y1; y < y2; y++) {
      map[x2][y] = map[x2][y + 1];
      minVal = Math.min(minVal, map[x2][y]);
    }

    // 오른쪽
    for (let x = x2; x > x1; x--) {
      map[x][y2] = map[x - 1][y2];
      minVal = Math.min(minVal, map[x][y2]);
    }

    // 위
    for (let y = y2; y > y1; y--) {
      map[x1][y] = map[x1][y - 1];
      minVal = Math.min(minVal, map[x1][y]);
    }

    map[x1][y1 + 1] = firstVal;
    res.push(minVal);
  });

  return res;
}

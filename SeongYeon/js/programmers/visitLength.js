function solution(dirs) {
  const move = { U: [-1, 0], D: [1, 0], L: [0, -1], R: [0, 1] };
  const passed = [];
  let row = 5,
    col = 5,
    res = 0;

  for (dir of dirs) {
    const prevRow = row;
    const prevCol = col;

    row += move[dir][0];
    col += move[dir][1];

    if (row < 0 || row > 10 || col < 0 || col > 10) {
      row = prevRow;
      col = prevCol;
      continue;
    }

    const path = `${prevRow}${prevCol}-${row}${col}`;
    const revPath = `${row}${col}-${prevRow}${prevCol}`;

    if (!passed.includes(path) && !passed.includes(revPath)) {
      res++;
      passed.push(path);
    }
  }

  return res;
}

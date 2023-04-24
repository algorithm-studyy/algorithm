function solution(dirs) {
  const move = { U: [-1, 0], D: [1, 0], L: [0, -1], R: [0, 1] };
  const passed = new Set();
  let row = 0,
    col = 0;

  for (dir of dirs) {
    const prevRow = row;
    const prevCol = col;

    row += move[dir][0];
    col += move[dir][1];

    if (row < -5 || row > 5 || col < -5 || col > 5) {
      row = prevRow;
      col = prevCol;
      continue;
    }

    passed.add(`${prevRow}${prevCol}-${row}${col}`);
    passed.add(`${row}${col}-${prevRow}${prevCol}`);
  }

  return passed.size / 2;
}

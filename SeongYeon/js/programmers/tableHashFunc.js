function solution(data, col, row_begin, row_end) {
  data.sort((prev, next) =>
    prev[col - 1] === next[col - 1]
      ? next[0] - prev[0]
      : prev[col - 1] - next[col - 1]
  );

  const answer = data.reduce((acc, cur, idx, src) => {
    if (row_begin <= idx + 1 && row_end >= idx + 1) {
      return (
        acc ^ src[idx].reduce((acc1, cur1) => acc1 + (cur1 % (idx + 1)), 0)
      );
    }
    return acc;
  }, 0);

  return answer;
}

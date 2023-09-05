function solution(triangle) {
  const height = triangle.length;
  let max = 0;

  const dfs = (depth, idx, sum) => {
    if (depth >= height) {
      max = Math.max(max, sum);
      return;
    }

    dfs(depth + 1, idx, sum + triangle[depth][idx]);
    dfs(depth + 1, idx + 1, sum + triangle[depth][idx]);
  };

  dfs(0, 0, 0);

  return max;
}

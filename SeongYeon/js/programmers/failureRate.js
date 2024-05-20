function solution(N, stages) {
  const failed = new Array(N + 1).fill(0);
  const reached = new Array(N + 1).fill(0);
  const ratio = new Array(N);
  const answer = [];

  stages.forEach((stage) => {
    failed[stage - 1] += 1;
    for (let i = 0; i < stage; i++) {
      reached[i] += 1;
    }
  });

  for (let i = 0; i < N; i++) {
    ratio[i] = failed[i] / reached[i];
  }

  ratio.forEach((value, index) => {
    answer.push({ index, value });
  });

  return answer.sort((a, b) => b.value - a.value).map((res) => res.index + 1);
}

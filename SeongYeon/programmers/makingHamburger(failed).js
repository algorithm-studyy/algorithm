function solution(ingredient) {
  let answer = 0;
  let prevAnswer = -1;

  while (answer !== prevAnswer) {
    let stacked = [];
    let stackedIdx = [];
    prevAnswer = answer;

    for (let i in ingredient) {
      if (ingredient[i] !== 4) {
        stacked.push(ingredient[i]);
        stackedIdx.push(i);
        if (stacked.length === 4) {
          if (stacked.join('') === '1231') {
            answer++;
            stackedIdx.forEach((idx) => {
              ingredient[idx] = 4;
            });
            stacked = [];
            stackedIdx = [];
          } else {
            stacked.shift();
            stackedIdx.shift();
          }
        }
      }
    }
  }
  return answer;
}

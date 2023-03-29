function solution(n) {
  let answer = 1;

  for (let i = 1; i <= n / 2; i++) {
    let sum = i;
    let add = i + 1;

    while (sum < n) {
      sum += add;
      add += 1;
    }

    if (sum === n) answer += 1;
  }

  return answer;
}

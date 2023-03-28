function solution(s) {
  const answer = [0, 0];

  while (s.length > 1) {
    let numOfOne = 0;
    for (let i = 0; i < s.length; i++) {
      s[i] === '1' ? numOfOne++ : answer[1]++;
    }
    s = numOfOne.toString(2);
    answer[0]++;
  }

  return answer;
}

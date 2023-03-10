function solution(s) {
  let answer = 1;
  let sameCnt = 0;
  let notSameCnt = 0;
  let startWord = s[0];
  for (let i = 0; i < s.length; i++) {
    if (s[i] === startWord) sameCnt++;
    else notSameCnt++;
    if (sameCnt === notSameCnt && i !== s.length - 1) {
      answer++;
      startWord = s[i + 1];
    }
  }
  return answer;
}

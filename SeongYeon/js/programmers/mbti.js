function solution(survey, choices) {
  let answer = '';
  const mbti = ['RT', 'CF', 'JM', 'AN'];
  const scores = { R: 0, T: 0, C: 0, F: 0, J: 0, M: 0, A: 0, N: 0 };

  for (let i in survey) {
    const score = choices[i] - 4;
    if (score < 0) scores[survey[i][0]] -= score;
    else if (score > 0) scores[survey[i][1]] += score;
  }

  mbti.forEach((type) => {
    if (scores[type[0]] < scores[type[1]]) answer += type[1];
    else answer += type[0];
  });

  return answer;
}

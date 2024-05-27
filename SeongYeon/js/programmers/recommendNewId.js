function solution(new_id) {
  const step4 = new_id
    .toLowerCase()
    .replaceAll(/[^a-z0-9-_.]+/g, '')
    .replaceAll(/[.]{2,}/g, '.')
    .replaceAll(/^[.]/g, '')
    .replaceAll(/[.]$/g, '');

  let answer = step4 || 'a';

  if (answer.length > 15) {
    answer = answer.at(14) === '.' ? answer.slice(0, 14) : answer.slice(0, 15);
  }

  if (answer.length < 3) {
    answer += answer.at(-1).repeat(3 - answer.length);
  }

  return answer;
}

function solution(babbling) {
  let answer = 0;
  const able = ['ye', 'ma', 'aya', 'woo'];

  babbling.forEach((word) => {
    let isAble = true;
    let prev = '';
    let i = 0;

    while (i < word.length) {
      const two = word.slice(i, i + 2);
      const three = word.slice(i, i + 3);

      if (able.includes(two) && prev !== two) {
        prev = two;
        i += 2;
      } else if (able.includes(three) && prev !== three) {
        prev = three;
        i += 3;
      } else {
        isAble = false;
        break;
      }
    }

    if (isAble) answer++;
  });

  return answer;
}

function solution(n, words) {
  const answer = [0, 0];
  const wordList = [words[0]];

  for (let i = 1; i < words.length; i++) {
    const lastWord = words[i - 1][words[i - 1].length - 1];
    if (words[i][0] !== lastWord || wordList.includes(words[i]))
      return [(i % n) + 1, parseInt(i / n) + 1];

    wordList.push(words[i]);
  }

  return answer;
}

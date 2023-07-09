function mostCommonWord(paragraph: string, banned: string[]): string {
  const lowerCase = paragraph.toLowerCase();
  const replaced = lowerCase.replace(/[^a-z]/gi, ' ');
  const wordList = replaced.split(' ');
  const notBannedList = wordList.filter(
    (word) => word && !banned.includes(word)
  );

  const wordCount = {};
  let maxCount = 0;
  let answer = '';

  notBannedList.forEach((word) => {
    if (wordCount[word]) wordCount[word]++;
    else wordCount[word] = 1;

    if (wordCount[word] > maxCount) {
      maxCount = wordCount[word];
      answer = word;
    }
  });

  return answer;
}

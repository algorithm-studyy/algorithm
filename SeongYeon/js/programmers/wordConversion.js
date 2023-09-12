String.prototype.isDifferOne = function (target) {
  let difference = 0;

  for (let i in target) {
    if (this[i] !== target[i]) difference += 1;
    if (difference > 1) return false;
  }

  return !!difference;
};

function solution(begin, target, words) {
  if (!words.includes(target)) return 0;

  const visited = [];
  let minCount = 0;

  const dfs = (word, count) => {
    if (word === target) {
      minCount = minCount === 0 ? count : Math.min(minCount, count);
      return;
    }

    for (let i in words) {
      if (!visited[i] && word.isDifferOne(words[i])) {
        visited[i] = true;
        dfs(words[i], count + 1);
        visited[i] = false;
      }
    }
  };

  for (let i in words) {
    if (begin.isDifferOne(words[i])) {
      visited[i] = true;
      dfs(words[i], 1);
      visited[i] = false;
    }
  }

  return minCount;
}

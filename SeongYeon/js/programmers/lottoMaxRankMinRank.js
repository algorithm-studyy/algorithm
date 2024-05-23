function solution(lottos, win_nums) {
  const myLotto = new Array(46).fill(false);
  let erased = 0;
  let match = 0;

  lottos.forEach((number) => {
    if (number === 0) {
      erased += 1;
      return;
    }

    myLotto[number] = true;
  });

  win_nums.forEach((winNumber) => {
    if (myLotto[winNumber]) match += 1;
  });

  return [Math.min(7 - (match + erased), 6), Math.min(7 - match, 6)];
}

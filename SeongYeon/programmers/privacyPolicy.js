function solution(today, terms, privacies) {
  let answer = [];
  const termsObj = {};
  const todayDate = new Date(today);

  terms.forEach((term) => {
    const tuple = term.split(' ');
    termsObj[tuple[0]] = Number(tuple[1]);
  });

  privacies.forEach((privacy, idx) => {
    const tuple = privacy.split(' ');
    const expDate = new Date(tuple[0]);
    const term = termsObj[tuple[1]];
    expDate.setMonth(expDate.getMonth() + term);

    if (todayDate >= expDate) answer.push(idx + 1);
  });

  return answer;
}

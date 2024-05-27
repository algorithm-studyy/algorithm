function solution(board, moves) {
  let answer = 0;
  const n = board.length;
  const notEmptyIndex = new Array(n).fill(n);
  const stack = [];

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (notEmptyIndex[j] === n && board[i][j]) notEmptyIndex[j] = i;
    }
  }

  for (let i = 0; i < moves.length; i++) {
    const moveIndex = moves[i] - 1;
    if (notEmptyIndex[moveIndex] === n) continue;

    stack.push(board[notEmptyIndex[moveIndex]][moveIndex]);
    notEmptyIndex[moveIndex] += 1;

    if (stack.length > 1 && stack.at(-1) === stack.at(-2)) {
      answer += 2;
      stack.pop();
      stack.pop();
    }
  }

  return answer;
}

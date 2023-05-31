function solution(n, apeachInfo) {
  // 1. 각 점에서 (어피치 < 라이언) 이어야만 점수 한번 획득, 둘다 0이면 없음
  // 2. (어피치 < 라이언) 일때만 이기고, 가장 큰 점수차로 이겨야됨
  // 3. 화살 n개는 다 소모해야됨
  // 4. 답이 여러개일 땐 가장 낮은 점수 많이 맞춘 걸로
  // 5. 점수 배열은 [10, 9, 8..., 0] 순서임
  const apeachStartScore = apeachInfo.reduce(
    (acc, cur, idx) => (cur > 0 ? acc + (10 - idx) : acc),
    0
  );
  const rionInfo = new Array(11).fill(0);
  let maxGap = 0;
  let answer = [];

  const getRionScore = (idx, depth, apeachScore, rionScore) => {
    if (depth === n) {
      if (apeachScore < rionScore && rionScore - apeachScore >= maxGap) {
        maxGap = rionScore - apeachScore;
        answer = [...rionInfo];
      }
      return;
    }
    if (idx === 11) return;

    rionInfo[idx] += 1;

    let addScore = 0;
    let minusScore = 0;

    if (apeachInfo[idx] < rionInfo[idx]) {
      addScore = 10 - idx;
      if (apeachInfo[idx] !== 0) {
        minusScore = 10 - idx;
      }
    }

    getRionScore(
      idx,
      depth + 1,
      apeachScore + minusScore,
      rionScore + addScore
    );
    getRionScore(
      idx + 1,
      depth + 1,
      apeachScore + minusScore,
      rionScore + addScore
    );

    rionInfo[idx] -= 1;
  };

  getRionScore(i, 0, apeachStartScore, 0);

  return answer.some((item) => item > 0) ? answer : [-1];
}

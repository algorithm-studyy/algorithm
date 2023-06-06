function solution(cap, n, deliveries, pickups) {
  let needToGo = 0;
  let answer = 0;

  for (let i in deliveries) {
    if (deliveries[n - i - 1] !== 0 || pickups[n - i - 1] !== 0) {
      needToGo = n - i;
      break;
    }
  }

  while (needToGo > 0) {
    let deliverCap = cap;
    let pickupCap = cap;

    answer += needToGo * 2;

    for (let i = needToGo - 1; i >= 0; i--) {
      if (deliverCap === 0 && pickupCap === 0) break;
    }
  }

  return answer;
}

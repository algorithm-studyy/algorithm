function solution(cap, n, deliveries, pickups) {
  let deliverIdx = -1;
  let pickupIdx = -1;
  let answer = 0;

  for (let i in deliveries) {
    if (deliveries[n - i - 1] !== 0) {
      deliverIdx = n - i - 1;
      break;
    }
  }

  for (let i in pickups) {
    if (pickups[n - i - 1] !== 0) {
      pickupIdx = n - i - 1;
      break;
    }
  }

  while (deliverIdx >= 0 || pickupIdx >= 0) {
    let deliverCap = cap;
    let pickupCap = cap;

    while (deliveries[deliverIdx] === 0) {
      deliverIdx--;
    }

    while (pickups[pickupIdx] === 0) {
      pickupIdx--;
    }

    answer += (Math.max(deliverIdx, pickupIdx) + 1) * 2;

    while (deliverIdx >= 0 && deliverCap !== 0) {
      if (deliveries[deliverIdx] > deliverCap) {
        deliveries[deliverIdx] -= deliverCap;
        deliverCap = 0;
      } else {
        deliverCap -= deliveries[deliverIdx];
        deliveries[deliverIdx] = 0;
        deliverIdx -= 1;
      }
    }

    while (pickupIdx >= 0 && pickupCap !== 0) {
      if (pickups[pickupIdx] > pickupCap) {
        pickups[pickupIdx] -= pickupCap;
        pickupCap = 0;
      } else {
        pickupCap -= pickups[pickupIdx];
        pickups[pickupIdx] = 0;
        pickupIdx -= 1;
      }
    }
  }

  return answer;
}

function arrayPairSum(nums: number[]): number {
  return nums
    .sort((a, b) => a - b)
    .reduce((acc, cur, idx) => (idx % 2 === 0 ? acc + cur : acc), 0);
}

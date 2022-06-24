var findAverage = function (nums) {
  return nums.reduce((p, c) => p + c, 0) / nums.length;
}

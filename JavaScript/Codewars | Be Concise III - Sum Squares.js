# 1
function sumSquares(array) {
  return array.reduce((a, b) => a + b ** 2, 0);
}

# 2
function sumSquares(array) {
  var arrSquar = array.map(n => n ** 2);
  return arrSquar.reduce((partialSum, a) => partialSum + a, 0);
}

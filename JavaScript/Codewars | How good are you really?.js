function betterThanAverage(classPoints, yourPoints) {
  const sum = (a, b) => a + b;
  return classPoints.reduce(sum) / classPoints.length < yourPoints
}

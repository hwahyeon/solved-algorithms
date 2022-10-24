function vectorLength(vector){
  x1 = vector[0][0]
  x2 = vector[1][0]
  y1 = vector[0][1]
  y2 = vector[1][1]
  return Math.hypot((x2-x1), (y2-y1))
}

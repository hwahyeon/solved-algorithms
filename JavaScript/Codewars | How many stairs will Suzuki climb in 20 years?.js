function stairsIn20(s){
  return 20 * s.reduce((a, b) => a + b.reduce((c, d) => c + d, 0), 0)
}

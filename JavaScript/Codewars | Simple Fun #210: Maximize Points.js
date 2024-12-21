function maximizePoints(team1, team2) {
  let point = 0
  const team1_sort = [...team1].sort((a, b) => a - b)
  const team2_sort = [...team2].sort((a, b) => a - b)

  let i = 0, j = 0;
  while (i < team1_sort.length && j < team2_sort.length) {
    if (team1_sort[i] > team2_sort[j]) {
      point++;
      j++;
    }
    i++;
  }
  return point
}

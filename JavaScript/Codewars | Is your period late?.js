function periodIsLate(last, today, cycleLength){
  return Math.floor(today.getTime() - last.getTime()) / (24 * 60 * 60 * 1000) > cycleLength
}

function warnTheSheep(queue) {
  const ind = queue.indexOf('wolf') + 1;
  const n = queue.length
  
  if (ind === n) {return "Pls go away and stop eating my sheep"}
  else {return `Oi! Sheep number ${n - ind}! You are about to be eaten by a wolf!`}
}

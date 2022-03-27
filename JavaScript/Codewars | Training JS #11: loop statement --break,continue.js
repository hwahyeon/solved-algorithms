function grabDoll(dolls){
  var bag=[];

  for (const element of dolls) {
    if (bag.length >= 3) {
      break
    } else if (element === 'Hello Kitty' || element === 'Barbie doll') {
      bag.push(element)
    } else {
      continue
    }
  }
  return bag;
}

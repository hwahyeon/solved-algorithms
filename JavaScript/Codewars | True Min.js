function min(a, b){
  if (isNaN(a)||isNaN(b)){
    return NaN;
  }
  if (a === null){a = 0}
  if (b === null){b = 0}
    return (a<b)?a:b;
}

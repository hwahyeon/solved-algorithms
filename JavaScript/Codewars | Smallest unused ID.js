function nextId(ids){
  const arr = [...new Set(ids)].sort(function(a, b){return a - b;});
  
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== i) {return i}
  }
  return arr.length;
}

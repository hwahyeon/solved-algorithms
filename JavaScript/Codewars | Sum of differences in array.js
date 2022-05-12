function sumOfDifferences(arr) {
  const list = arr.sort(function(a, b) {return a - b;})
  
  let res = 0
  for (let i = 0; i < list.length - 1; i++) {
    res += (list[i] - list[i+1])
  }
  return -1*res
}

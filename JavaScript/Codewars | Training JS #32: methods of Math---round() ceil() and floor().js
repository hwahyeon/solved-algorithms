function roundIt(n){
  var o = n.toString().split('.');
  let n1 = o[0].length
  let n2 = o[1].length
  if (n1 < n2){
    return Math.ceil(n)
  } else if (n1 > n2){
    return Math.floor(n)
  } else {
    return Math.round(n)
  }
}

function noBoringZeros(n) {
  if (n < 0) { res = -1 } 
  else       { res = 1 }
  
  n = String(n).replace('-', '').split("").reverse().join("")
  n = Number(n)
  n = String(n).split("").reverse().join("")
  return res * Number(n)
}

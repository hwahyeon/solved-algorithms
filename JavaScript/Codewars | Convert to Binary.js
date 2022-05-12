function toBinary(n){
  let num = n;
  let res = String(num%2);
  while (num > 1){
    num = parseInt(num/2);
    res += String(num%2);
  }
  return Number( res.split('').reverse().join('') );
}

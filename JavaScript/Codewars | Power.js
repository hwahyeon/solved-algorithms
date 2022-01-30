function numberToPower(number, power){
  var res = 1;
  for( var i = 1 ; i <= power ; i++ ){
    res = res * number
  }
  return res
}

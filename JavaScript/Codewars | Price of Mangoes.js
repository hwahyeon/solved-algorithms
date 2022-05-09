function mango(quantity, price){
  return ( parseInt(quantity/3)*2 + quantity%3 ) * price;
}

function howManySmaller(arr,n){
  return arr.filter(x => x.toFixed(2) < n).length;
}

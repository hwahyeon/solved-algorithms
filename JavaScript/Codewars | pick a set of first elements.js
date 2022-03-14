function first(arr, n) {
  if (n === undefined){
    return arr.slice(undefined, 1);
  } else {
    return arr.slice(undefined, n);    
  }
}

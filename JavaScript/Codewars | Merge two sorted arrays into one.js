function mergeArrays(arr1, arr2) {

  const set = new Set(arr1.concat(arr2));
  const arr = [...set];
  
  return arr.sort(function(a, b) {
                  return a - b;
                  });
}

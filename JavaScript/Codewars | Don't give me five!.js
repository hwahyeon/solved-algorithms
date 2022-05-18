function dontGiveMeFive(start, end){
  let cnt = 0;
  for (let i = start; i < end + 1; i++){
    if(!String(i).includes('5')){
      cnt += 1
    }  
  }
  return cnt
}

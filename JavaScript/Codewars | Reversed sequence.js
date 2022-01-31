const reverseSeq = n => {
  const res = [];
  for(let i = n ; i > 0 ; i -= 1){
    res.push(i);
  }
  return res;
};

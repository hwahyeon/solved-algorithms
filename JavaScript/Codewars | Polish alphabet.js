function correctPolishLetters(string) {
  let res = string;
  const pol = ['ą','ć','ę','ł','ń','ó','ś','ź','ż']
  const eng = ['a','c','e','l','n','o','s','z','z']
  
  for(let i = 0; i < 9; i++){
    res = res.replace(pol[i], eng[i]);
  }
  return res.replace('ł', 'l').replace('ą', 'a');
}

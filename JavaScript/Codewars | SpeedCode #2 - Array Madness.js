function arrayMadness(a, b) {
  let suma = 0;
  let sumb = 0;
  
  for (let i = 0; i < a.length; i++){suma += a[i]**2}
  for (let i = 0; i < b.length; i++){sumb += b[i]**3}
  
  return suma > sumb;
}

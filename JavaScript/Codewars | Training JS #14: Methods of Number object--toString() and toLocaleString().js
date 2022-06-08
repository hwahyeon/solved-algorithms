function colorOf(r,g,b){
  const hr = r.toString(16).padStart(2,'0'),
        hg = g.toString(16).padStart(2,'0'),
        hb = b.toString(16).padStart(2,'0')
  
  return `#${hr}${hg}${hb}`
}

function uefaEuro2016(teams, scores){
  let res = `At match ${teams[0]} - ${teams[1]}, `
  
  if      (scores[0] === scores[1]) {res += `teams played draw.`}
  else if (scores[0] > scores[1])   {res += `${teams[0]} won!`}
  else                              {res += `${teams[1]} won!`}
  return res
}

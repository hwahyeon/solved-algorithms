function getDrinkByProfession(param){
  const obj = {
    'jabroni' : "Patron Tequila",
    'school counselor' : "Anything with Alcohol",
    'programmer' : "Hipster Craft Beer",
    'bike gang member' : "Moonshine",
    'politician' :"Your tax dollars",
    'rapper' :"Cristal"
  }
  const DRINK = param.toLowerCase()
  if (DRINK in obj) {return obj[DRINK]}
  else {return 'Beer'}
}

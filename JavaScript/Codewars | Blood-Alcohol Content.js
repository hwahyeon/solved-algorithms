function bloodAlcoholContent(drinks, weight, sex, time){
  let r;
  if(sex === 'male'){r = 0.73} else {r = 0.66}
  let bac = (drinks.ounces * drinks.abv * 5.14 / weight * r) - 0.015 * time
  return parseFloat(bac.toFixed(4));
}

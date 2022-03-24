function howManydays(month){
  var days;
  switch (true){
      case [1,3,5,7,8,10,12].includes(month):
        days = 31;
        break;
      case [4,6,9,11].includes(month):
        days = 30;
        break;
      case 2 == month:
        days = 28;
        break;
  }
  return days;
}

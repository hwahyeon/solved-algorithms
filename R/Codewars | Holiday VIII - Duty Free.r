duty_free <- function(price, discount, holiday_cost){
 floor(holiday_cost / (price*discount*0.01))
}

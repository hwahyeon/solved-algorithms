to24hourtime <- function(hour, minute, period){
       if(period == 'am' & hour == 12){hour <- 0}
  else if(period == 'pm' & hour != 12){hour <- hour+12}
  paste0(sprintf("%02d", hour), sprintf("%02d", minute))
}

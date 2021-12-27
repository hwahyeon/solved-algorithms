switch_it_up <- function(number){
  ifelse(number == 0, 'Zero',
         c('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')[number])
}

#
switch_it_up <- function(number){
 c('One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')[number+1]
}

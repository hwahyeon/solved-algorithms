library(stringr)

bumps <- function(road){
       if(str_count(road, 'n')<=15){"Woohoo!"}
  else if(str_count(road, 'n')>15){"Car Dead"}
}

human_years_cat_years_dog_years <- function(human_years){
        if(human_years==1){c(1,15,15)}
   else if(human_years==2){c(2,24,24)}
   else {c(human_years,24+(human_years-2)*4,24+(human_years-2)*5)}
}

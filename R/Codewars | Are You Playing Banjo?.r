are_you_playing_banjo <- function(name){
  if(tolower(substr(name, 1, 1)) == 'r'){paste(name,'plays banjo')}
  else {paste(name,'does not play banjo')}
}

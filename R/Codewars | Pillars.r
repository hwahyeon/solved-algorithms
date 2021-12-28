pillars = function(num_of_pillars, distance, width) {
  ifelse(num_of_pillars==1, 0, (num_of_pillars-1)*distance*100 + (num_of_pillars-2)*width)
}

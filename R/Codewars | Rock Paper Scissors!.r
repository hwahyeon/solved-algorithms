rps <- function(p1, p2){
  if(p1 == p2){'Draw!'}
  else if((p1 == 'scissors' & p2 == 'paper')|(p1 == 'paper' & p2 == 'rock')|(p1 == 'rock' & p2 == 'scissors')){'Player 1 won!'}
  else{'Player 2 won!'}
}

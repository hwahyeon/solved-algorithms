PROGRAM P21633
  IMPLICIT NONE
  REAL :: A, X
  READ(*,*) A
  X = A * 0.01 + 25
  
  if (X .LT. 100) then
    WRITE(*,"(I10)") 100
  elseif (X .GT. 2000) then
    WRITE(*,"(I10)") 2000
  else
    WRITE(*,"(F10.2)") X
  endif

END PROGRAM P21633

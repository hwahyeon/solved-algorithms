PROGRAM P6825
  IMPLICIT NONE
  REAL :: A, B, X
  READ(*,*) A
  READ(*,*) B
  X = A / (B * B)

  if (X .LT. 18.5) then
    WRITE(*,'(A)') 'Underweight'
  elseif (X .GT. 25) then
    WRITE(*,'(A)') 'Overweight'
  else
    WRITE(*,'(A)') 'Normal weight'
  endif

END PROGRAM P6825

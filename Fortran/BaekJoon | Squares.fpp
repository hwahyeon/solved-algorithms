PROGRAM P6887
  IMPLICIT NONE
  INTEGER :: A
  READ(*,*) A
  WRITE (*,"(A,' ',I0,A)") 'The largest square has side length', INT(A**0.5), '.'
END PROGRAM P6887

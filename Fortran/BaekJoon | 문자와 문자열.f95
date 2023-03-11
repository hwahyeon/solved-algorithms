PROGRAM P27866
    IMPLICIT NONE
    CHARACTER(len=1001):: s
    INTEGER:: n
    READ(*,*) s
    READ(*,*) n
    
    WRITE(*,'(a)') s(n:n)
END PROGRAM P27866

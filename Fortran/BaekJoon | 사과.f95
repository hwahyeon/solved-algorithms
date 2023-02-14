PROGRAM P10833
    IMPLICIT NONE
    INTEGER:: a, b, n, i, T = 0
    
    READ(*,*) n
    DO i=1, n
        READ(*,*) a, b
        T = T + MOD(b, a) 
    END DO
    
    WRITE(*,'(I0)') T
END PROGRAM P10833

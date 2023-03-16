PROGRAM P10569
    IMPLICIT NONE
    INTEGER:: i, n, V, E
    
    READ(*,*) n
    DO i=1, n
        READ(*,*) V, E
        WRITE(*,'(I0)') 2 - V + E
    END DO
END PROGRAM P10569

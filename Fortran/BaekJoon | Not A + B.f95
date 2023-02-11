PROGRAM P23530
    IMPLICIT NONE
    INTEGER:: N, i, A, B

    READ(*,*) N
    DO i = 1, N
        READ(*,*) A, B
        WRITE(*, '(I0)') 1
    END DO
END PROGRAM P23530

PROGRAM P11134
    IMPLICIT NONE
    INTEGER:: T, i, N, C, R
    READ(*,*) T
    DO i = 1, T
        READ(*,*) N, C
        if (mod(N, C) .EQ. 0) then
            R = 0
        else
            R = 1
        END if
        WRITE(*,'(I0)') N/C + R
    END DO
END PROGRAM P11134

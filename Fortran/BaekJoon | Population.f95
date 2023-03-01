PROGRAM P26561
    IMPLICIT NONE
    INTEGER :: N, p, t, i, inc, dec
    READ(*,*) N
    DO i=1, N
        READ(*,*) p, t
        inc = t/4
        dec = t/7
        WRITE(*, '(I0)') p + inc - dec
    END DO
END PROGRAM P26561

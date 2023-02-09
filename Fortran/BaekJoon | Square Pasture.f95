PROGRAM P14173
    IMPLICIT NONE
    INTEGER :: x1, y1, x2, y2, x3, y3, x4, y4, R1, R2, T
    READ(*,*) x1, y1, x2, y2
    READ(*,*) x3, y3, x4, y4
    R1 = max(x2, x4) - min(x1, x3)
    R2 = max(y2, y4) - min(y1, y3)
    T = max(R1, R2)
    WRITE(*, '(I0)') T*T
END PROGRAM

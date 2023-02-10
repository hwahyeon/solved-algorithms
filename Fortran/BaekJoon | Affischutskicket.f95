PROGRAM P24183
    IMPLICIT NONE
    REAL :: A, B, C, R1, R2, R3
    READ(*,*) A, B, C
    R1 = 229 * 324 * A * 2
    R2 = 297 * 420 * B * 2
    R3 = 210 * 297 * C
    WRITE(*, '(f0.6)') (R1 + R2 + R3) * 0.000001

END PROGRAM P24183

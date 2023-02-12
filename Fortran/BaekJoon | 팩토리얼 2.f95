PROGRAM P27433
INTEGER N, I
INTEGER(selected_int_kind(16)) F
    READ(*,*) N

    F = 1
    DO 10 I=1, N, 1
        F = F * I
10 continue
    WRITE(*, '(I0)') F
    STOP

END PROGRAM P27433

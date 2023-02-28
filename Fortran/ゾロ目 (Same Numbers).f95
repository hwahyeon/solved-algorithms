PROGRAM P27324
    INTEGER A, B, N
    READ(*,*) N
    A = N / 10
    B = mod(N, 10)
    
    if (A .EQ. B) then
        WRITE(*, '(I0)') 1
    else
        WRITE(*, '(I0)') 0
    end if
END PROGRAM P27324

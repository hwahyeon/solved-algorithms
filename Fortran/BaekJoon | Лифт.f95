program P27262
    IMPLICIT NONE
    INTEGER :: n, k, a, b
    
    READ(*, *) n, k, a, b

    WRITE(*, '(I0," ",I0)') abs(1 - k)*b + (n - 1)*b, (n - 1)*a
end program P27262

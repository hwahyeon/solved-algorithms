PROGRAM P27332
    INTEGER A, B, R
    READ(*,*) A
    READ(*,*) B
    R = B * 7 + A
    if (R .LE. 30) then
        WRITE(*, '(I0)') 1
    else
        WRITE(*, '(I0)') 0
    end if
END PROGRAM P27332

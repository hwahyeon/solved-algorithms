PROGRAM P27328

    INTEGER :: A, B
    READ(*,*) A
    READ(*,*) B
    if (A .EQ. B) then
        WRITE(*, '(I0)') 0
    elseif (A .LT. B) then
        WRITE(*, '(I0)') -1
    else
        WRITE(*, '(I0)') 1
    end if
    
END PROGRAM P27328

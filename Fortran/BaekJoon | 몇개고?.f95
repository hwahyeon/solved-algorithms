PROGRAM P27294
    INTEGER T, S
    READ(*,*) T, S
    
    if ((T .GE. 12) .AND. (T .LE. 16) .AND. (S .EQ. 0)) then
        WRITE(*, '(I0)') 320
    else
        WRITE(*, '(I0)') 280
    end if
END PROGRAM P27294

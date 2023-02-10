PROGRAM P1977
    IMPLICIT NONE
    INTEGER :: i, j, r, min, idx
    READ(*,*) i
    READ(*,*) j

    r = 0
    min = 0
    idx = 0

    DO i=i, j
        if(i**0.5 .EQ. INT(i**0.5)) then
            idx = idx + 1
            r = r + i
            if(idx .EQ. 1) then
                min = i
            END if
        END if
    END DO
    
    if(min .EQ. 0) then
        WRITE(*, '(I0)') -1
    else
        WRITE(*, '(I0)') r
        WRITE(*, '(I0)') min
    END if
END PROGRAM P1977

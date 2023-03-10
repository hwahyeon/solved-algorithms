PROGRAM P24079
    IMPLICIT NONE
    INTEGER:: x, y, z
    
    READ(*,*) x
    READ(*,*) y
    READ(*,*) z
    if (z .LT. x+y) then
        WRITE(*,'(I0)') 0
    else
        WRITE(*,'(I0)') 1
    END if
END PROGRAM P24079

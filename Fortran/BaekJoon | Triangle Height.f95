PROGRAM P26592
    IMPLICIT NONE
    INTEGER:: n, i
    CHARACTER(len=12) :: fmt
    REAL:: a, b, h

    READ(*,*) n
    
    DO i=1, n
        READ(*,*) a, b
        h = 2*a/b

        if (h < 1) then
            fmt = '(a,(F4.2),a)'
        else
            fmt = '(a,(F0.2),a)'
        end if
        
        WRITE(*,fmt) 'The height of the triangle is ', h, ' units'
    END DO
END PROGRAM P26592

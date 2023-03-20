PROGRAM P27257
    IMPLICIT NONE
    INTEGER:: i, r, n
    CHARACTER(len=10):: s
    
    READ(*,*) s
    n = len(TRIM(s))
    r = n
    DO i=1, n
        if (s(n+1-i:n+1-i) .EQ. '0') then
            r = r - 1
        else
            EXIT
        END if
    END DO
    
    DO i=1, n
        if (s(i:i) .NE. '0') then
            r = r - 1
        END if
    END DO
    
    WRITE(*,'(I0)') r
END PROGRAM P27257

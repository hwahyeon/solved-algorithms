PROGRAM P27213
    IMPLICIT NONE
    INTEGER(KIND=8):: m, n
    
    READ(*,*) m
    READ(*,*) n
    if (m .EQ. 1) then
        WRITE(*,'(I0)') n
    else if (n .EQ. 1) then
        WRITE(*,'(I0)') m
    else
        WRITE(*,'(I0)') (2 * (m+n)) - 4
    END if
END PROGRAM P27213

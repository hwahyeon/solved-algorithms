PROGRAM P27541
    IMPLICIT NONE
    INTEGER:: n
    CHARACTER(len=100):: s
    
    READ(*,*) n
    READ(*,*) s
    
    if (s(n:n) .EQ. 'G') then
        WRITE(*,'(a)') s(1:n-1)
    else
        WRITE(*,'(a)') TRIM(s)//'G'
    END if
END PROGRAM P27541

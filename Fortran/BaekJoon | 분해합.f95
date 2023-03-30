PROGRAM P2231
    IMPLICIT NONE
    INTEGER:: n, i, j, r
    
    READ(*,*) n
    
    DO j = 1, n
        i = j
        r = i
        do while(i .NE. 0)
            r = r + MOD(i, 10)
            i = i / 10            
        end do
        if (r .EQ. n) then
            WRITE(*,'(I0)') j
            EXIT
        end if
        if (j .EQ. n) then
            WRITE(*,'(I0)') 0
        end if
    END DO

END PROGRAM P2231

PROGRAM P23972
    REAL(selected_int_kind(38)):: k, n
    
    READ(*,*) k, n
    if (n .EQ. 1) then
        WRITE(*,'(I0)') -1
    else
        if (MOD((k*n), (n-1)) .NE. 0) then
            WRITE(*,'(I0)') INT((k*n)/(n-1) +1)
        else
            WRITE(*,'(I0)') INT((k*n)/(n-1))
        END if
    END if
END PROGRAM P23972

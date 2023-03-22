PROGRAM P5341
    INTEGER n
    
    DO WHILE (1 .EQ. 1)
        READ(*,*) n
        if (n .EQ. 0) then
            EXIT
        END if
        WRITE(*,'(I0)') n * (n+1) / 2
    END DO
END PROGRAM P5341

program P19774
    INTEGER :: n, t, a, b

    READ(*,*) n
    DO i=1, n
        READ(*,*) t
        a = (t / 100) ** 2
        b = (MOD(t, 100)) ** 2
        
        if (MOD((a + b), 7) .EQ. 1) then
            WRITE(*,'(a)') 'YES'
        else
            WRITE(*,'(a)') 'NO'
        END if
    END DO
end program P19774

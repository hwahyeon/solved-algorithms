program P2721
    INTEGER :: n, t, res

    READ(*,*) n
    DO i=1, n
        res=0
        READ(*,*) t
        DO j=1, t
            res = res + j*(j+1)*(j+2)/2
        END DO
        WRITE(*,'(I0)') res
    END DO

end program P2721

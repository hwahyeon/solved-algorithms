PROGRAM P24623

    REAL:: n, a
    
    READ(*,*) n
    READ(*,*) a
    WRITE(*,'(I0)') INT((180 - a)/2 + a/2)
    
END PROGRAM P24623

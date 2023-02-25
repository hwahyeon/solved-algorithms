PROGRAM P24751

    IMPLICIT NONE
    REAL a
    
    READ(*,*) a
    WRITE(*,'(f0.10)') 100 / a
    WRITE(*,'(f0.10)') 100 / (100 - a)
    
END PROGRAM P24751

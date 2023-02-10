PROGRAM P2587
    IMPLICIT NONE
    INTEGER, DIMENSION(5) :: LIST
    INTEGER :: REPO, i, j
    READ(*,*) LIST(1)
    READ(*,*) LIST(2)
    READ(*,*) LIST(3)
    READ(*,*) LIST(4)
    READ(*,*) LIST(5)
    
! Bubble Sort
DO j=1, 10
    DO i=1, 4
        if (LIST(i) .GT. LIST(i+1)) then
            REPO = LIST(i)
            LIST(i) = LIST(i+1)
            LIST(i+1) = REPO
        END if
    END DO
END DO
    
    WRITE(*, '(I0)') (LIST(1) + LIST(2) + LIST(3) + LIST(4) + LIST(5))/5
    WRITE(*, '(I0)') LIST(3)
END PROGRAM P2587

PROGRAM P10250
    IMPLICIT NONE
    INTEGER:: i, j, h, w, n, floor
    READ(*,*) j
    DO i = 1, j
        READ(*,*) h, w, n
        floor = mod(n, h)
        if (floor .EQ. 0) then
            WRITE(*,'(I0)') h * 100 + (n/h)
        else
            WRITE(*,'(I0)') floor * 100 + (n/h) + 1
        END if
    END DO
END PROGRAM P10250

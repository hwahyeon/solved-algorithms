PROGRAM P8719
    INTEGER:: a, b, c, i
    READ(*,*) n
    DO i=1, n
        READ(*,*) a, b
        c = 0
        do while (a .LT. b)
            a = a * 2
            c = c + 1
        end do
        WRITE(*,'(I0)') c
    END DO
END PROGRAM P8719

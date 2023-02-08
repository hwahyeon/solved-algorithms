PROGRAM P26332
    INTEGER:: N, i, S, D

    READ(*,*) N
    DO i = 1, N
        READ(*,*) S, D
        WRITE(*, '(I0,a,I0)') S, ' ', D
        if (S .GE. 2) then
            WRITE(*, '(I0)') S*D - 2*(S-1)
        else
            WRITE(*, '(I0)') S*D
       end if
    END DO
END PROGRAM P26332

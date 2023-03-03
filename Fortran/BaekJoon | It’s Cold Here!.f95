PROGRAM P6830
    CHARACTER(len=256):: C, res = ''
    REAL:: d, min = 200

    DO WHILE (.TRUE.)
        READ(*,*) C, d
        if (d .LT. min) then
            min = d
            res = C
        END if
        if (TRIM(C) .EQ. 'Waterloo') then
            EXIT
        END if
    END DO
    WRITE(*,'(a)') res
END PROGRAM P6830

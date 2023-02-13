program P9366
    INTEGER :: n, a, b, c

    READ(*,*) n
    DO i=1, n
        READ(*,*) a, b, c
        if ((a+b > c) .AND. (a+c > b) .AND. (b+c > a)) then
            if ((a .EQ. b) .AND. (b .EQ. c) .AND. (a .EQ. c)) then
                WRITE(*,'(a,I0,a)') 'Case #', i ,': equilateral'
            elseif ((a .EQ. b) .OR. (b .EQ. c) .OR. (a .EQ. c)) then
                WRITE(*,'(a,I0,a)') 'Case #', i ,': isosceles'
            else
                WRITE(*,'(a,I0,a)') 'Case #', i ,': scalene'
            END if
        else
            WRITE(*,'(a,I0,a)') 'Case #', i ,': invalid!'
        END if
    END DO

end program P9366

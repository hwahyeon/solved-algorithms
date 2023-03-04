PROGRAM P27245
    IMPLICIT NONE
    INTEGER w, l, h
    
    READ(*,*) w
    READ(*,*) l
    READ(*,*) h
    
    if((MIN(w, l)/h >= 2) .AND. (MAX(w, l, h)/min(w, l, h) >= 2)) then
        WRITE(*, '(a)') 'good'
    else
        WRITE(*, '(a)') 'bad'
    END if
    
END PROGRAM P27245

PROGRAM P9772
    IMPLICIT NONE
    REAL :: X, Y
    
    DO WHILE (.TRUE.)
        READ(*,*) X, Y
        if (X .EQ. 0 .AND. Y .EQ. 0) then
            WRITE(*,'(a)') 'AXIS'
            EXIT
        else if (X .EQ. 0 .OR. Y .EQ. 0) then
            WRITE(*,'(a)') 'AXIS'
        else if (X .GT. 0 .AND. Y .GT. 0) then
            WRITE(*,'(a)') 'Q1'
        else if (X .LT. 0 .AND. Y .GT. 0) then
            WRITE(*,'(a)') 'Q2'
        else if (X .LT. 0 .AND. Y .LT. 0) then
            WRITE(*,'(a)') 'Q3'
        else if (X .GT. 0 .AND. Y .LT. 0) then
            WRITE(*,'(a)') 'Q4'
        END if
    END DO
    
END PROGRAM P9772

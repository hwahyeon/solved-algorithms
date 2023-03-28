PROGRAM P1002
  IMPLICIT NONE
  REAL :: x1, y1, r1, x2, y2, r2
  REAL :: d
  INTEGER :: n, i

  READ(*,*) n
  
  DO i = 1, n
    READ(*,*) x1, y1, r1, x2, y2, r2
    
    d = SQRT((x1 - x2)**2 + (y1 - y2)**2)
    
    IF (d == 0) THEN
      IF (r1 == r2) THEN
        WRITE(*,'(I0)') -1
      ELSE
        WRITE(*,'(I0)') 0
      END IF
    ELSE
      IF (r1 + r2 == d .OR. ABS(r2 - r1) == d) THEN
        WRITE(*,'(I0)') 1
      ELSE IF (r1 + r2 > d .AND. ABS(r1 - r2) < d) THEN
        WRITE(*,'(I0)') 2
      ELSE
        WRITE(*,'(I0)') 0
      END IF
    END IF
  END DO
  
END PROGRAM P1002

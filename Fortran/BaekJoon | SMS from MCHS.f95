PROGRAM P21638
    IMPLICIT NONE
    INTEGER:: t1, v1, t2, v2
    
    READ(*,*) t1, v1
    READ(*,*) t2, v2
    
    if (t2.LT.0 .AND. v2.GE.10) then
        WRITE(*,'(a)') "A storm warning for tomorrow! Be careful and stay home if possible!"
    elseif (t1.GT.t2) then
        WRITE(*,'(a)') "MCHS warns! Low temperature is expected tomorrow."
    elseif (v1.LT.v2) then
        WRITE(*,'(a)') "MCHS warns! Strong wind is expected tomorrow."
    else
        WRITE(*,'(a)') "No message"
    END if
END PROGRAM P21638

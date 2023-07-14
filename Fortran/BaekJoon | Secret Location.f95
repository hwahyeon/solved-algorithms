program P5340
    IMPLICIT NONE
    INTEGER :: l(6), i
    CHARACTER(len=100) :: s

    do i = 1, 6
        read(*,'(A)') s
        l(i) = len_trim(s)
    end do

    WRITE(*,'(a,I0,a,I0,a,I0)') 'Latitude ', l(1), ':', l(2), ':', l(3)
    WRITE(*,'(a,I0,a,I0,a,I0)') 'Longitude ', l(4), ':', l(5), ':', l(6)
end program P5340

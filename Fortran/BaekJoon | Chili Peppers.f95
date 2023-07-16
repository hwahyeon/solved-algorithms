program P28249
    implicit none
    character(len=10) :: t
    integer :: i, n, r = 0

    read(*, *) n
    do i = 1, n
        read(*, '(A)') t
             if (t .EQ. 'Poblano') then
            r = r + 1500
        else if (t .EQ. 'Mirasol') then
            r = r + 6000
        else if (t .EQ. 'Serrano') then
            r = r + 15500
        else if (t .EQ. 'Cayenne') then
            r = r + 40000
        else if (t .EQ. 'Thai') then
            r = r + 75000
        else if (t .EQ. 'Habanero') then
            r = r + 125000
        end if
    end do

    write(*, '(I0)') r

end program P28249

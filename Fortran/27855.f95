program P27855
    implicit none
    integer :: h1, b1, h2, b2, p1, p2
    character(len=10) :: ans

    read(*, *) h1, b1
    read(*, *) h2, b2

    p1 = 3 * h1 + b1
    p2 = 3 * h2 + b2

    if (p1 > p2) then
        write(*, '(a, I0)') "1 ", p1 - p2
        ans = "1 " 
    else if (p1 < p2) then
        write(*, '(a, I0)') "2 ", p2 - p1
    else if (p1 .EQ. p2) then
        write(*, '(A)') "NO SCORE" 
    end if

end program P27855

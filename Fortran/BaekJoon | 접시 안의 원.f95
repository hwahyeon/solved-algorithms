program P16483
    implicit none
    real :: h

    read(*, *) h
    h = h / 2.0

    write(*, '(I0)') int(h * h + 0.5)
end program P16483

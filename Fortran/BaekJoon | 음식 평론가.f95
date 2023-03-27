PROGRAM P1188
  implicit none
  integer :: n, m, g
  
  READ(*,*) n, m
  
  g = gcd(n, m)
  write(*,'(I0)') m - g
  
contains
  recursive function gcd(a, b) result(res)
    INTEGER, INTENT(in) :: a, b
    INTEGER:: res
    
    if (mod(a,b) == 0) then
      res = b
    else
      res = gcd(b, mod(a,b))
    end if
  end function gcd
END PROGRAM P1188

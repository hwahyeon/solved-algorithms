! Solution
module Solution
  implicit none
contains
  logical pure function check_for_factor(base, factor) result (res)
    integer, intent(in) :: base, factor
    res = .false.
    if (mod(base, factor) .EQ. 0) then
      res = .true.    
    END if
  end function check_for_factor
end module Solution

! Sample Tests
program TestCases
  use CW2
  use Solution
  
  implicit none
  
  call describe("Check for factor")
    call it("basic tests")
      call assertEquals(.true., check_for_factor(10, 2))
      call assertEquals(.true., check_for_factor(63, 7))
      call assertEquals(.true., check_for_factor(2450, 5))
      call assertEquals(.true., check_for_factor(24612, 3))
      call assertEquals(.false., check_for_factor(9, 2))
      call assertEquals(.false., check_for_factor(653, 7))
      call assertEquals(.false., check_for_factor(2453, 5))
      call assertEquals(.false., check_for_factor(24617, 3))
    call endContext()
  call endContext()
end program

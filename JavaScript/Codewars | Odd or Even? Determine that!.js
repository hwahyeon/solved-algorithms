function oddOrEven(n) {
  const odd = Math.round(n / 2)
  if (n % 2 != 0) {
    return 'Either'
  } else if (odd % 2 == 0) {
    return 'Even'
  } else {
    return 'Odd'
  }
}

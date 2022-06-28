function isPalindrome(line) {
  return line.toString() == line.toString().split('').reverse().join('');
}

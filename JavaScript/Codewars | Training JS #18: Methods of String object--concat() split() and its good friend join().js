function splitAndMerge(string, separator) {
  return string.split(' ').map(e => e.split('').join(separator)).join(' ');
}

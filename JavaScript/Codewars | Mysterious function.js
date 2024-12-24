var getNum = function(n) {
  return [...n.toString()].reduce((r, c) => r + (c === '8' ? 2 : '069'.includes(c) ? 1 : 0), 0);
};

const isReallyNaN = (val) => {
  // return isNaN(val);  // wasn't working as planned :-(
  return val !== val;
};

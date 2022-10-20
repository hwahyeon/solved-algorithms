function runYourString (arg, obj) {
  return new Function(obj.param, obj.func)(arg);
}

function validateUsr(username) {
  const reg = /^[a-z0-9_]{4,16}$/;
  return reg.test(username);
}

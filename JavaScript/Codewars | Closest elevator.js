function elevator(left, right, call){
  const l = Math.abs(call - left)
  const r = Math.abs(call - right)
  return l < r ? 'left' : 'right'
}

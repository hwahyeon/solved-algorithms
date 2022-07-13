function calculateTip(amount, rating) {
  const r = rating.toLowerCase()
       if (r == 'excellent') {return Math.ceil(amount * 0.2)}
  else if (r == 'great') {return Math.ceil(amount * 0.15)}
  else if (r == 'good') {return Math.ceil(amount * 0.1)}
  else if (r == 'poor') {return Math.ceil(amount * 0.05)}
  else if (r == 'terrible') {return Math.ceil(amount * 0)}
  else {return 'Rating not recognised'}
}

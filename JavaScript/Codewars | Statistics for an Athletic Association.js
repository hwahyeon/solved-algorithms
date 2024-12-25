function stat(strg) {
  if (strg === ''){
    return ''
  }
  
  const arr = strg.split(',').map(record => {
    const [h, m, s] = record.split('|').map(Number);
    return h * 3600 + m * 60 + s;
  });

  const sortedArr = [...arr].sort((a, b) => a - b);

  const average = Math.floor(arr.reduce((sum, value) => sum + value, 0) / arr.length)

  const mid = Math.floor(sortedArr.length / 2);
  const median = sortedArr.length % 2 === 0
    ? Math.floor((sortedArr[mid - 1] + sortedArr[mid]) / 2)
    : sortedArr[mid];

  const range = Math.floor(sortedArr[sortedArr.length - 1] - sortedArr[0])

  function formatTime(seconds) {
    const hours = String(Math.floor(seconds / 3600)).padStart(2, '0')
    const minutes = String(Math.floor((seconds % 3600) / 60)).padStart(2, '0')
    const remainingSeconds = String(seconds % 60).padStart(2, '0')

    return `${hours}|${minutes}|${remainingSeconds}`
  }

  return `Range: ${formatTime(range)} Average: ${formatTime(average)} Median: ${formatTime(median)}`
}

function humanReadable (seconds) {
  const hour = Math.floor(seconds / 3600);
  const minute = Math.floor((seconds % 3600) / 60);
  const second = seconds % 60;

  const format = (t) => t.toString().padStart(2, '0');

  return `${format(hour)}:${format(minute)}:${format(second)}`;
}

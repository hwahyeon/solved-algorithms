SELECT
  id,
  network(ip_address) as first_address,
  broadcast(ip_address) as last_address
FROM connections
ORDER BY id;

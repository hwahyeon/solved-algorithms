CREATE FUNCTION increment (i integer)
  RETURNS integer as $$
BEGIN
  RETURN i+1;
END;
$$ language plpgsql;

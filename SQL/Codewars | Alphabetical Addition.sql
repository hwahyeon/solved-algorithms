CREATE OR REPLACE FUNCTION Alpha(n integer)
RETURNS TEXT AS $$
DECLARE
    i INTEGER;
BEGIN
    IF n is null THEN
        return CHR(122);
    ELSEIF n < 27 THEN
        return CHR(n+96);
    ELSE
        WHILE n > 26 LOOP
            n := n - 26;
        END LOOP;
        return CHR(n+96);
    END IF;
END;
$$ LANGUAGE plpgsql;


SELECT
  Alpha(SUM(ASCII(letter)-96)::INTEGER) as letter
FROM
  letters;

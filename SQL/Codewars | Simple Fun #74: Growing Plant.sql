CREATE OR REPLACE FUNCTION plant(down int, up int, desired_height int)
RETURNS INTEGER AS $$
DECLARE
    day INTEGER := 0;
    height INTEGER := 0;
BEGIN
    WHILE height <= desired_height
    LOOP
        height := height + up;
        day := day + 1;
            IF height < desired_height THEN
                height := height - down;
            ELSE
                RETURN day;
            END IF;
    END LOOP;
    RETURN day;
END;
$$ LANGUAGE plpgsql;

SELECT
  id,
  plant(down_speed, up_speed, desired_height) as num_days
FROM growing_plant;

SELECT
  unnest(string_to_array(REGEXP_REPLACE(text, '[aeiou]', '!', 'g'), '!')) as results
FROM random_string;

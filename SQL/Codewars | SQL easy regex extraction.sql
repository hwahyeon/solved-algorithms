SELECT
  name,
  greeting,
  replace(
    substring(greeting from '#[0-9]+'), '#', '') as user_id
FROM greetings

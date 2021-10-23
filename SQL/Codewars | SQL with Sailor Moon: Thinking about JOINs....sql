SELECT
  senshi_name as sailor_senshi,
  real_name_jpn as real_name,
  cats.name as cat,
  school
FROM sailorsenshi
  LEFT JOIN schools ON sailorsenshi.school_id=schools.id
  LEFT JOIN cats ON sailorsenshi.cat_id=cats.id

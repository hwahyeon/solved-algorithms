SELECT pok.pokemon_name, pok.str * multipliers.multiplier as modifiedStrength, multipliers.element
FROM pokemon as pok INNER JOIN multipliers
ON pok.element_id = multipliers.id
where pok.str * multipliers.multiplier >= 40
ORDER BY modifiedStrength DESC

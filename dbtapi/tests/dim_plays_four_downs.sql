SELECT
    *
FROM
    {{ ref('dim_plays_clean') }}
WHERE 
    down > 4
LIMIT 10
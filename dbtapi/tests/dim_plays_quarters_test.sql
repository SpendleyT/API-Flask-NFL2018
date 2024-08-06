SELECT 
    * 
FROM 
    {{ ref('dim_plays_clean') }}
WHERE quarter > 5
LIMIT 10
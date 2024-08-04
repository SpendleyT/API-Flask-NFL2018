WITH src_players AS (
	SELECT * FROM {{ ref('src_players') }}
)
SELECT 
	playerid AS player_id,
	position AS position,
    split_part(displayname, ' ', 1) AS first_name,
    split_part(displayname, ' ', 2) AS last_name,
	displayname as full_name,
	collegename AS college
FROM
	src_players
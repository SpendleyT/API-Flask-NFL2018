WITH raw_players AS (
	SELECT * FROM public.players
)
SELECT 
	playerid AS player_id,
	position AS position,
	displayname as full_name,
	split_part(displayname, ' ', 1) AS first_name,
	split_part(displayname, ' ', 2) AS last_name,
	collegename AS college
FROM
	raw_players
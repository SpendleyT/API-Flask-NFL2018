WITH raw_players AS (
	SELECT * FROM public.players
)
SELECT 
	playerid AS player_id,
	position AS position,
	displayname as full_name,
	collegename AS college
FROM
	raw_players
WITH raw_players AS (
	SELECT * FROM public.players
)
SELECT 
	playerid,
	position,
	displayname,
	collegename
FROM
	raw_players
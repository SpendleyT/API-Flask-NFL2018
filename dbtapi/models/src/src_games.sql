WITH raw_games AS (
	SELECT * FROM public.games
)
SELECT 
	gameid as game_id,
	gamedate as game_date,
	gametime as start_time,
	hometeam as home,
	awayteam as away,
	week
FROM
	raw_games
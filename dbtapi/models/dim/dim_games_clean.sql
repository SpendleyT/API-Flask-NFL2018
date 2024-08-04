with src_games as (
    SELECT * FROM {{ ref('src_games') }}
)
SELECT
    game_id,
	game_date,
	start_time AT TIME ZONE 'UTC' AS est_start_time,
	home,
	away,
	week
FROM
	src_games
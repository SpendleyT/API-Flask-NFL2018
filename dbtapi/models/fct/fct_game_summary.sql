{{
    config(
        materialized = 'incremental',
        on_schema_change = 'fail'
    )
}}
WITH src_plays AS (
    SELECT * FROM {{ ref('dim_plays_clean') }}
),
src_games AS (
    SELECT * FROM {{ ref('dim_games_clean') }}
) 
SELECT
    src_plays.game_id,
    src_games.game_date,
    src_games.home,
    src_games.away,
    max(src_plays.away_score) as away_final,
    max(src_plays.home_score) as home_final
FROM
    src_plays join src_games 
	on src_games.game_id = src_plays.game_id
{% if is_incremental() %}
    WHERE game_date > (select max(game_date) from {{ this }})
{% endif %}
GROUP BY 
    src_plays.game_id,
    src_games.game_date,
    src_games.home,
    src_games.away

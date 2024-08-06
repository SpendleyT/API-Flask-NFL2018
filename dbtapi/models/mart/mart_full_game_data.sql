{{ config(
    materialized = 'table'
)}}

WITH fct_game_summary AS (
    SELECT * FROM {{ ref('fct_game_summary' )}}
),
team_names AS (
    SELECT * FROM {{ ref('team_names') }}
)
SELECT
    fct_game_summary.game_id,
    fct_game_summary.game_date,
    fct_game_summary.home,
    (SELECT CONCAT (team_names.location, ' ', team_names.name) FROM team_names 
        WHERE team = fct_game_summary.home) AS home_name,
    fct_game_summary.home_final,
    fct_game_summary.away,
    (SELECT CONCAT (team_names.location, ' ', team_names.name) FROM team_names 
        WHERE team = fct_game_summary.away) AS away_name,
    fct_game_summary.away_final
FROM 
    fct_game_summary JOIN team_names
    ON fct_game_summary.home = team_names.team

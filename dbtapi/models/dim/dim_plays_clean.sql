WITH src_plays AS (
	SELECT * FROM {{ ref('src_plays') }}
)
SELECT 
	play_id,
	game_id,
	description AS play_summary,
	quarter,
	down,
	distance,
	on_offense,
	CASE 
        WHEN play_type = 'play_type_pass' THEN 'completed pass'
        WHEN play_type = 'play_type_sack' THEN 'QB sacked'
    ELSE
        'incomplete pass'
    END
	yardlineside,
	yardlinenumber,
	offenseformation AS off_formation,
	personnelo AS off_personnel,
	defendersinthebox AS def_box,
	numberofpassrushers AS def_rushers,
	personneld AS def_personnel,
	CASE 
        WHEN typedropback is null THEN 'TRADITIONAL'
        WHEN typedropback = 'Unknown' THEN 'TRADITIONAL'
    ELSE
        typedropback
    END AS drop_back,
	presnapvisitorscore AS presnap_away_score,
	presnaphomescore AS presnap_home_score,
	gameclock as clock,
	penaltycodes as penalties,
	penaltyjerseynumbers as players_flagged,
	CASE 
        WHEN passresult is null THEN 'R'
    ELSE
        passresult
    END as pass_result,
	offenseplayresult AS play_yardage,
	epa,
	isdefensivepi AS is_dpi
FROM
	src_plays
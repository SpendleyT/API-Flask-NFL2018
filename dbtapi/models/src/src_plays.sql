WITH raw_plays AS (
	SELECT * FROM public.plays
)
SELECT 
	playid AS play_id,
	gameid AS game_id,
	playdescription AS description,
	quarter,
	down,
	yardstogo AS distance,
	possessionteam AS on_offense,
	playtype AS play_type,
	yardlineside,
	yardlinenumber,
	offenseformation AS off_formation,
	personnelo AS off_personnel,
	defendersinthebox AS def_box,
	numberofpassrushers AS def_rushers,
	personneld AS def_personnel,
	typedropback AS drop_back,
	presnapvisitorscore AS presnap_away_score,
	presnaphomescore AS presnap_home_score,
	gameclock as clock,
	penaltycodes as penalties,
	penaltyjerseynumbers as players_flagged,
	passresult as pass_result,
	offenseplayresult AS off_play_result,
	playresult AS play_result,
	epa as epa,
	isdefensivepi AS is_dpi
FROM
	raw_plays
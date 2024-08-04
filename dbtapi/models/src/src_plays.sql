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
	offenseformation,
	personnelo,
	defendersinthebox,
	numberofpassrushers,
	personneld,
	typedropback,
	presnapvisitorscore,
	presnaphomescore,
	gameclock,
	penaltycodes,
	penaltyjerseynumbers,
	passresult,
	offenseplayresult,
	playresult,
	epa,
	isdefensivepi
FROM
	raw_plays
DROP TABLE IF EXISTS plays;
DROP TABLE IF EXISTS week_data;

CREATE TABLE plays (
	gameid bigint,
	playid int,
	playdescription VARCHAR,
	quarter integer,
	down integer,
	yardstogo integer,
	possessionteam varchar(4),
	playtype varchar(30),
	yardlineside varchar(4),
	yardlinenumber integer,
	offenseformation varchar(30),
	personnelO varchar(50),
	defendersinthebox integer,
	numberofpassrushers integer,
	personnelD varchar(50),
	typedropback varchar(50),
	presnapvisitorscore integer,
	presnaphomescore integer,
	gameclock varchar(8),
	absoluteyardnumber integer,
	penaltycodes varchar(20),
	penaltyjerseynumbers varchar(20),
	passresult varchar(10),
	offenseplayresult varchar(10),
	playresult varchar(10),
	epa numeric(18,15),
	isdefensivepi boolean
);

CREATE TABLE week_data (
	time timestamp with time zone,
	x numeric(5,2),
	y numeric(5,2),
	s numeric(5,2),
	a numeric(5,2),
	dis numeric(5,2),
	o numeric(5,2),
	dir numeric(5,2),
	event varchar(30),
	nflid varchar(20),
	displayname varchar(70),
	jerseynumber varchar(2),
	position varchar(4),
	frameid varchar(3),
	team varchar(12),
	gameid bigint,
	playid bigint,
	playdirection varchar(20),
	route varchar(50)
);

SELECT * FROM week_data;
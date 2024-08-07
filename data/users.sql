DROP TABLE IF EXISTS dbtapi.users;

CREATE TABLE dbtapi.users (
	user_id varchar(20) PRIMARY KEY,
	username varchar(50) UNIQUE NOT NULL,
	user_pwd varchar(50) NOT NULL,
	user_group varchar(20) NOT NULL
);
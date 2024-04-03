CREATE DATABASE datetime_queries;
USE datetime_queries;

--  --------------CREATING TABLE and POPULATING WITH DATA -----------------------

	CREATE TABLE uber_rides(
    ride_id INTEGER PRIMARY KEY auto_increment ,
	user_id INTEGER,
    cab_id INTEGER,
    start_time DATETIME , 
    end_time DATETIME 
    );
    SELECT * FROM uber_rides;
    
	INSERT INTO uber_rides (user_id ,cab_id , start_time , end_time) VALUES
    (1 , 1, '2023-03-09 08:00:00' , '2023-03-09 09:00:00');
    INSERT INTO uber_rides (user_id ,cab_id , start_time , end_time) VALUES
    (1 , 1, '2023-03-09 23:00:00' , '2023-03-09 00:30:00');
    INSERT INTO uber_rides (user_id ,cab_id , start_time , end_time) VALUES
    (5 , 31, '2023-03-11 19:00:00' , '2023-03-09 20:30:00'),
    (6 , 33 , '2023-03-12 18:00:00' , '2023-03-12 18:30:00');
    
	INSERT INTO uber_rides (user_id ,cab_id , start_time , end_time) VALUES
    (9 , 3, '2023-03-15 2:00:00' , '2023-03-15 3:30:00');

-- ------------- DATETIME FUNCTIONs -------------------------------------
	SELECT CURRENT_DATE();
    SELECT CURRENT_TIME();
    SELECT NOW();
    
	INSERT INTO uber_rides (user_id ,cab_id , start_time , end_time) VALUES
    (10 , 7, '2023-03-15 2:00:00' , NOW());
    
    SELECT * FROM uber_rides;
	
-- ---------------------- EXTRACTION Functions --------------------------

	-- q1 fetching date from start column
		SELECT * , DATE(start_time) FROM uber_rides;
		
	-- q2 Fetch time from start_time col
		SELECT *, TIME(start_time) FROM uber_rides;
    
	-- q3 Fetching YEAR from start_time col
		SELECT *, YEAR(start_time) FROM uber_rides;
		
	-- Q4 Fetching Month and Monthname
		SELECT * , MONTH(start_time) , MONTHNAME(start_time) FROM uber_rides;
		
	-- Q5 Fetching day of month , week and day name
		SELECT DAY(start_time) , DAYOFWEEK(start_time) , DAYNAME(start_time)
		FROM uber_rides;
		
	-- Q6 fetch which quarter
		SELECT QUARTER(start_time) FROM uber_rides;
		
	-- Q7 Fetch hour , min , sec
		SELECT HOUR(start_time) , MINUTE(start_time) , SECOND(start_time)
		FROM uber_rides;
		
	-- q8 FETCH day of the year
		SELECT DAYOFYEAR(start_time) FROM uber_rides;
		
	-- q9 Fetch week of the year
		 SELECT WEEKOFYEAR(start_time) FROM uber_rides;
		 
	-- q10 FETCH last date of month
		SELECT LAST_DAY(start_time) FROM uber_rides;


-- ------------------- DATETIME formatting ----------------
	-- REFER TO DOCUMENTATION
	-- doc - https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html#function_date-format
	-- EX1  DATE FORMAT
		SELECT start_time , DATE_FORMAT(start_time , '%d-%b-%y' ) FROM uber_rides;
		
	-- EX2 change the 24 hour to 12 hour AND no seconds
		SELECT start_time , DATE_FORMAT(start_time , '%l:%i %p') FROM uber_rides;

-- --------------------- TYPE CONVERSION -----------------------
	-- IMPLICIT	(even though they were string but mysql able to understand but no always)
		SELECT '2023-03-11' > '2023-03-09';
	
	-- EXPLICIT(but mysql wont be able to understand this)
		SELECT MONTHNAME('9 Mar 2023');
	-- HENCE USE STR_TO_DATE() FN (tell the format which wrong date is in)
		SELECT str_to_date('9 Mar 2023' , '%e %b %Y');
		
-- ---------------- DATETIME ARTHIMATIC OPERATION--------------------
-- Q1 find how many days has been passed since the course
	SELECT DATEDIFF(CURRENT_DATE() , '2022-11-07');

-- Q2 FIND DIFF BETWEEN TIME
	SELECT TIMEDIFF(CURRENT_TIME() , '20:00:00');
	SELECT TIMEDIFF(end_time , start_time)
    FROM uber_rides;
		
-- Q3 FIND DATE EXACTLY AFTER 10 YEARS(USE DATE_ADD)
	SELECT date_add(NOW() , INTERVAL 10 YEAR)
-- Q4 DATE_SUB() similar to date_sum()
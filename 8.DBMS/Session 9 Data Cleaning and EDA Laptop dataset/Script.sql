CREATE DATABASE data_cleaning;
USE data_cleaning;
CREATE TABLE laptop_backup LIKE laptops;

INSERT INTO laptop_backup
SELECT * FROM laptops;

SELECT * FROM laptop_backup;

SELECT DATA_LENGTH/1024 FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'data_cleaning' AND TABLE_NAME = 'laptops';

ALTER TABLE laptops DROP COLUMN `Unnamed: 0`;
SELECT * FROM laptops;

-- Step 1: Create a temporary table to store index values
CREATE TEMPORARY TABLE temp_index AS
SELECT `index`
FROM laptops
WHERE Company IS NULL 
  AND TypeName IS NULL 
  AND Inches IS NULL 
  AND ScreenResolution IS NULL 
  AND Cpu IS NULL 
  AND RAM IS NULL 
  AND Memory IS NULL 
  AND Gpu IS NULL 
  AND OpSys IS NULL 
  AND Weight IS NULL 
  AND PRICE IS NULL;

DELETE FROM laptops WHERE `index` IN 
(SELECT * FROM temp_index);

SELECT COUNT(*) FROM laptops;
SELECT * FROM laptops;

WITH ram_update AS 
(SELECT `index` ,  REPLACE(Ram , 'GB' , '') AS ram2 FROM laptops)

UPDATE laptops t1
SET Ram = (SELECT ram2 FROM ram_update t2
WHERE t1.index = t2.index);

ALTER TABLE laptops MODIFY COLUMN Ram INTEGER;

DELETE FROM laptops
WHERE Inches = '?' ;

ALTER TABLE laptops MODIFY COLUMN Inches DECIMAL(10 , 1);


UPDATE laptops l1
SET Price = ROUND(Price);

UPDATE laptop_backup l1
SET Ram = REPLACE(Ram , 'GB' , '') ;

SELECT * FROM laptop_backup;

ALTER TABLE laptops MODIFY COLUMN Price INTEGER;

SELECT OpSys,
CASE 
		WHEN OpSys LIKE '%mac%' THEN 'macos'
		WHEN OpSys LIKE 'windows%' THEN 'windows'
		WHEN OpSys LIKE '%linux%' THEN 'linux'
		WHEN OpSys = 'No OS' THEN 'N/A'
		ELSE 'other'
END AS 'os_brand'
FROM laptops;

UPDATE laptops
SET OpSys = 
CASE 
	WHEN OpSys LIKE '%mac%' THEN 'macos'
	WHEN OpSys LIKE 'windows%' THEN 'windows'
	WHEN OpSys LIKE '%linux%' THEN 'linux'
	WHEN OpSys = 'No OS' THEN 'N/A'
	ELSE 'other'
END;

SELECT * FROM laptops;

ALTER TABLE laptops
ADD COLUMN gpu_brand VARCHAR(255) AFTER Gpu , 
ADD COLUMN gpu_name VARCHAR(255) AFTER gpu_brand;

SELECT SUBSTRING_INDEX(gpu , ' ' , 1) FROM laptops;

UPDATE laptops L1
SET gpu_brand = (
		SELECT SUBSTRING_INDEX(gpu , ' ' , 1) FROM (SELECT * FROM laptops) L2
		WHERE L1.index = L2.index
);

SELECT REPLACE(Gpu , gpu_brand , '') FROM laptops;
UPDATE laptops L1
SET gpu_name = REPLACE(Gpu , gpu_brand , '');

SELECT * FROM laptops;
ALTER TABLE laptops
ADD COLUMN cpu_brand VARCHAR(255) AFTER Cpu , 
ADD COLUMN cpu_name VARCHAR(255) AFTER cpu_brand,
ADD COLUMN cpu_speed DECIMAL(10 , 1) AFTER cpu_name;


UPDATE laptops
SET cpu_brand = SUBSTRING_INDEX(Cpu , ' ' , 1)
;

UPDATE laptops L1
SET cpu_speed = CAST(REPLACE(SUBSTRING_INDEX(Cpu , ' ' , -1),'GHz','') AS
	DECIMAL(10 ,1 ));

UPDATE laptops
SET cpu_name = REPLACE(REPLACE(Cpu,cpu_brand,''),SUBSTRING_INDEX(REPLACE(Cpu,cpu_brand,''),' ',-1),'');
					

SELECT * FROM laptops;

SELECT 
SUBSTRING_INDEX(SUBSTRING_INDEX(ScreenResolution , ' ', -1),'x' ,1),
SUBSTRING_INDEX(SUBSTRING_INDEX(ScreenResolution , ' ', -1),'x' ,-1) 
FROM laptops;

ALTER TABLE laptops
ADD COLUMN resolution_width INTEGER AFTER ScreenResolution,
ADD COLUMN resolution_height INTEGER AFTER resolution_width;

UPDATE laptops t1
SET 
resolution_width = SUBSTRING_INDEX(SUBSTRING_INDEX(ScreenResolution , ' ', -1),'x' ,1),
resolution_height = SUBSTRING_INDEX(SUBSTRING_INDEX(ScreenResolution , ' ', -1),'x' ,-1);


SELECT * FROM laptops;

ALTER TABLE laptops
ADD COLUMN touchscreen INTEGER AFTER resolution_height;

SELECT ScreenResolution Like '%Touch%' FROM laptops;
UPDATE laptops
SET touchscreen = ScreenResolution Like '%Touch%';
SELECT * FROM laptops; 

ALTER TABLE laptops
ADD COLUMN FALTU INTEGER AFTER resolution_height;
SELECT * FROM laptops; 

UPDATE laptops
SET FALTU = SUBSTRING_INDEX(SUBSTRING_INDEX(ScreenResolution , ' ', -1),'x' ,-1);

ALTER TABLE laptops
DROP COLUMN ScreenResolution,
DROP COLUMN FALTU;

ALTER TABLE laptops
DROP COLUMN Cpu,
DROP COLUMN Gpu;

SELECT SUBSTRING_INDEX(TRIM(cpu_name) , ' ',2) FROM laptops;
UPDATE laptops
SET cpu_name =  SUBSTRING_INDEX(TRIM(cpu_name) , ' ',2);

ALTER TABLE laptops
ADD COLUMN memory_type VARCHAR(255) AFTER Memory,
ADD COLUMN primary_storage INTEGER AFTER memory_type,
ADD COLUMN secondary_storage INTEGER AFTER primary_storage;

SELECT Memory,
CASE
	WHEN Memory LIKE '%SSD%' AND Memory LIKE '%HDD%' THEN 'Hybrid'
    WHEN Memory LIKE '%SSD%' THEN 'SSD'
    WHEN Memory LIKE '%HDD%' THEN 'HDD'
    WHEN Memory LIKE '%Flash Storage%' THEN 'Flash Storage'
    WHEN Memory LIKE '%Hybrid%' THEN 'Hybrid'
    WHEN Memory LIKE '%Flash Storage%' AND Memory LIKE '%HDD%' THEN 'Hybrid'
    ELSE NULL
END AS 'memory_type'
FROM laptops;

UPDATE laptops
SET memory_type = CASE
	WHEN Memory LIKE '%SSD%' AND Memory LIKE '%HDD%' THEN 'Hybrid'
    WHEN Memory LIKE '%SSD%' THEN 'SSD'
    WHEN Memory LIKE '%HDD%' THEN 'HDD'
    WHEN Memory LIKE '%Flash Storage%' THEN 'Flash Storage'
    WHEN Memory LIKE '%Hybrid%' THEN 'Hybrid'
    WHEN Memory LIKE '%Flash Storage%' AND Memory LIKE '%HDD%' THEN 'Hybrid'
    ELSE NULL
END;

SELECT * FROM laptops;

SELECT Memory,
REGEXP_SUBSTR(SUBSTRING_INDEX(Memory,'+',1),'[0-9]+'),
CASE WHEN Memory LIKE '%+%' THEN REGEXP_SUBSTR(SUBSTRING_INDEX(Memory,'+',-1),'[0-9]+') ELSE 0 END
FROM laptops;


UPDATE laptops
SET 
primary_storage = REGEXP_SUBSTR(SUBSTRING_INDEX(Memory,'+',1),'[0-9]+'),
secondary_storage = 
CASE WHEN Memory LIKE '%+%' THEN REGEXP_SUBSTR(SUBSTRING_INDEX(Memory,'+',-1),'[0-9]+') ELSE 0 END;



UPDATE laptops
SET primary_storage = CASE WHEN primary_storage <= 2 THEN primary_storage*1024 ELSE primary_storage END,
secondary_storage = CASE WHEN secondary_storage <= 2 THEN secondary_storage*1024 ELSE secondary_storage END;

SELECT * FROM laptops;

ALTER TABLE laptops DROP COLUMN gpu_name;
ALTER TABLE laptops DROP COLUMN Memory;
SELECT * FROM laptops;

SELECT t.buckets,REPEAT('*',COUNT(*)/5) FROM (SELECT price, 
CASE 
	WHEN price BETWEEN 0 AND 25000 THEN '0-25K'
    WHEN price BETWEEN 25001 AND 50000 THEN '25K-50K'
    WHEN price BETWEEN 50001 AND 75000 THEN '50K-75K'
    WHEN price BETWEEN 75001 AND 100000 THEN '75K-100K'
	ELSE '>100K'
END AS 'buckets'
FROM laptops) t
GROUP BY t.buckets;

SELECT t.buckets , REPEAT('*' , COUNT(*)/5) FROM (SELECT price , 
CASE 
	WHEN price BETWEEN 0 AND 25000 THEN '0-25K'
    WHEN price BETWEEN 25001 AND 50000 THEN '25K-50K'
    WHEN price BETWEEN 50001 AND 75000 THEN '50K-75K'
    WHEN price BETWEEN 75001 AND 100000 THEN '75K-100K'
	ELSE '>100K'
END AS 'buckets'
FROM laptops) t
GROUP BY t.buckets;

SELECT Company,
SUM(CASE WHEN cpu_brand = 'Intel' THEN 1 ELSE 0 END) AS 'intel',
SUM(CASE WHEN cpu_brand = 'AMD' THEN 1 ELSE 0 END) AS 'amd',
SUM(CASE WHEN cpu_brand = 'Samsung' THEN 1 ELSE 0 END) AS 'samsung'
FROM laptops
GROUP BY Company;

UPDATE laptops
SET price = NULL
WHERE `index` IN (7,869,1148,827,865,821,1056,1043,692,1114);

SELECT * FROM laptops
WHERE price IS NULL;

UPDATE laptops t1
SET t1.Price = (SELECT AVG(Price) FROM (SELECT * FROM laptops) t2) 
WHERE t1.Price IS NULL;


SELECT * FROM laptops
WHERE `index` IN (7,869,1148,827,865,821,1056,1043,692,1114);


UPDATE laptops T1
SET Price = (SELECT AVG(Price) FROM (SELECT * FROM laptops) T2
WHERE T1.Company = T2.Company )
WHERE Price IS NULL
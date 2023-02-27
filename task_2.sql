USE test_db;

SELECT
TRIM(SUBSTRING_INDEX(name,' ',1)) AS `Имя`, TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(name,' ',-2), ' ',1)) AS `Фамилия`, 
TRIM(SUBSTRING_INDEX(name,' ',-1)) AS `Отчество`
FROM customers;
USE shop_data;


-- Операторы, фильтрация, сортировка и ограничение
-- Задание № 1 
SELECT * FROM users;
UPDATE usersnew_created_at
SET updated_at = NOW() AND created_at = NOW()
LIMIT 100;
-- Задание № 2
ALTER TABLE users ADD new_created_at DATETIME;
UPDATE users SET new_created_at = STR_TO_DATE(created_at, '%d.%m.%Y %l:%i') LIMIT 100;
ALTER TABLE users DROP new_created_at, CHANGE new_created_at created_at DATETIME;

ALTER TABLE users ADD new_updated_at DATETIME;
UPDATE users SET new_updated_at = STR_TO_DATE(updated_at, '%d.%m.%Y %l:%i') LIMIT 100;
ALTER TABLE users DROP updated_at, CHANGE new_updated_at created_at DATETIME;
-- Задание № 3
SELECT value FROM storehouses_products
ORDER BY CASE 
			WHEN value = 0 
				THEN 1 
			ELSE 0 END, value;
-- Агрегация данных
-- Задание № 1
SELECT AVG(age) as avg_age FROM (SELECT Year(current_timestamp) - Year(birthday_at) AS age FROM users) AS age;
-- Задание № 2
SELECT
    DAYNAME(CONCAT(YEAR(NOW()), '-', SUBSTRING(birthday_at, 6, 10))) AS day_of_week,
    COUNT(*) AS count
FROM
    users
GROUP BY 
    day_of_week
ORDER BY
	count DESC;


USE shop_data;


-- Операторы, фильтрация, сортировка и ограничение
-- Задание № 1 
-- SELECT * FROM users;
-- UPDATE usersnew_created_at
-- SET updated_at = NOW() AND created_at = NOW()
-- LIMIT 100;
-- Задание № 2
-- ALTER TABLE users ADD new_created_at DATETIME;
-- UPDATE users SET new_created_at = STR_TO_DATE(created_at, '%d.%m.%Y %l:%i') LIMIT 100;
-- ALTER TABLE users DROP new_created_at, CHANGE new_created_at created_at DATETIME;

-- ALTER TABLE users ADD new_updated_at DATETIME;
-- UPDATE users SET new_updated_at = STR_TO_DATE(updated_at, '%d.%m.%Y %l:%i') LIMIT 100;
-- ALTER TABLE users DROP updated_at, CHANGE new_updated_at created_at DATETIME;
-- Задание № 3
SELECT value FROM storehouses_products
ORDER BY value;
-- Задание № 4
-- Задание № 5
-- Агрегация данных
-- Задание № 1

-- Задание № 2
-- Задание № 3


-- 1) В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. 
-- Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. 
-- Используйте транзакции.

START TRANSACTION;
INSERT IGNORE INTO sample.users
	SELECT * FROM shop.users WHERE id = 1;
COMMIT;

-- 2) Создайте представление, которое выводит название name товарной позиции 
-- из таблицы products и соответствующее название каталога name из 
-- таблицы catalogs.

CREATE OR REPLACE VIEW items AS 
	SELECT products.name AS prod_name, catalogs.name
		FROM products, catalogs 
        WHERE products.catalog_id = catalogs.id;
SELECT * FROM items;

-- 3)Создайте хранимую функцию hello(), которая будет возвращать приветствие, 
-- в зависимости от текущего времени суток. С 6:00 до 12:00 функция должна 
-- возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать 
-- фразу "Добрый день", с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".

DELIMITER //
CREATE PROCEDURE `hello`()
BEGIN
	CASE 
		WHEN CURTIME() BETWEEN '06:00:00' AND '12:00:00' THEN
			SELECT 'Доброе утро';
		WHEN CURTIME() BETWEEN '12:00:00' AND '18:00:00' THEN
			SELECT 'Добрый день';
		WHEN CURTIME() BETWEEN '18:00:00' AND '00:00:00' THEN
			SELECT 'Добрый вечер';
		ELSE
			SELECT 'Доброй ночи';
	END CASE;
END;

-- 2) В таблице products есть два текстовых поля: name с названием товара и description с его описанием. 
-- Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное 
-- значение NULL неприемлема. Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля 
-- были заполнены. При попытке присвоить полям NULL-значение необходимо отменить операцию.


DROP TRIGGER IF EXISTS prod_insert_trigg//
CREATE TRIGGER prod_trigg before insert on products
FOR EACH ROW
BEGIN
	IF (new.name is null) AND (new.description is null) THEN 
	SET new.name = 'default_name', new.description = 'default_text';
	END IF;
END//

DROP TRIGGER IF EXISTS prod_update_trigg//
CREATE TRIGGER prod_update_trigg BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
	IF (new.name is null) and (new.description is null) THEN 
	SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'name and description == NULL'; 
	END IF;
END//


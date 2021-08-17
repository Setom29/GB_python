-- Создайте таблицу logs типа Archive. 
-- Пусть при каждом создании записи в таблицах users, catalogs и products в таблицу logs 
-- помещается время и дата создания записи, название таблицы, идентификатор первичного ключа и содержимое поля

USE shop;

CREATE TABLE logs(
	created_at DATETIME,
	table_name VARCHAR(50),
	primary_key_id BIGINT,
	name_value VARCHAR(255)
) ENGINE=ARCHIVE;


DROP TRIGGER IF EXISTS users_log;
DROP TRIGGER IF EXISTS catalogs_log;
DROP TRIGGER IF EXISTS products_log;

DELIMITER //

CREATE TRIGGER users_log AFTER INSERT ON users
FOR EACH ROW 
BEGIN
	INSERT INTO logs (
		created_at, table_name, primary_key_id, name_value)
	VALUES (NOW(), 'users', NEW.id, NEW.name);
END//

CREATE TRIGGER catalogs_log AFTER INSERT ON catalogs
FOR EACH ROW 
BEGIN
	INSERT INTO logs (
		created_at, table_name, primary_key_id, name_value)
	VALUES (NOW(), 'catalogs', NEW.id, NEW.name);
END//

CREATE TRIGGER products_log AFTER INSERT ON products
FOR EACH ROW 
BEGIN
	INSERT INTO logs (
		created_at, table_name, primary_key_id, name_value)
	VALUES (NOW(), 'products', NEW.id, NEW.name);
END//


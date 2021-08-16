USE notes_bot;

DROP TRIGGER IF EXISTS telegram_id_check;


DELIMITER //

-- Проверка валидностb Telegram id. 

CREATE TRIGGER telegram_id_check BEFORE INSERT ON users
FOR EACH ROW
BEGIN
	IF NEW.telegram_id NOT BETWEEN 100000 AND 999999999 THEN
		SIGNAL SQLSTATE '45000' SET message_text = 'Некорректный id.';
	END IF;
END //



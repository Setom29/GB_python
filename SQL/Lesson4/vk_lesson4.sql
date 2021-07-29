USE vk;
-- повторение действий урока
ALTER TABLE friend_requests 
ADD CONSTRAINT sender_not_reciever_check
CHECK (from_user_id != to_user_id);

ALTER TABLE users 
ADD CONSTRAINT phone_check
CHECK (REGEXP_LIKE(phone, '^[0-9]{11}$'));

ALTER TABLE profiles 
ADD CONSTRAINT fk_profiles_media
FOREIGN KEY (photo_id) REFERENCES media (id);

-- запрос для переименования названий типов медиа

UPDATE `vk`.`media_types` SET `name` = 'image' WHERE (`id` = '1');
UPDATE `vk`.`media_types` SET `name` = 'audio' WHERE (`id` = '2');
UPDATE `vk`.`media_types` SET `name` = 'video' WHERE (`id` = '3');
UPDATE `vk`.`media_types` SET `name` = 'document' WHERE (`id` = '4');
SELECT * FROM media_types;

-- запрос, удаляющий заявки в друзья самому себе
DELETE FROM friend_requests
WHERE from_user_id = to_user_id;
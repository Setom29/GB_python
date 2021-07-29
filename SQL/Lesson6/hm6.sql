use vk;

-- Задание №2 по поиску пользователя, который больше всего общался с заданным.
SET @required_user_id = 1;

SELECT id, CONCAT(first_name, ' ', last_name) AS name FROM users WHERE id = (
	SELECT from_user_id
	FROM messages
	WHERE to_user_id = @required_user_id
	GROUP BY from_user_id
	ORDER BY COUNT(from_user_id) DESC
	LIMIT 1);

-- Задание №3
SELECT SUM(SUM_OF_LIKES) AS amount FROM 
	(SELECT IFNULL(posts_sum, 0) AS SUM_OF_LIKES, user_id,  COUNT(user_id) OVER (ORDER BY birthday DESC) AS cum_sum FROM profiles
	LEFT OUTER JOIN (SELECT user_id AS id, SUM(sum) AS posts_sum FROM posts
			JOIN (SELECT sum(like_type) AS sum, post_id FROM posts_likes GROUP BY post_id) AS likes
			ON posts.id = likes.post_id
			GROUP BY user_id) 
		AS total_likes
	ON profiles.user_id = total_likes.id
	GROUP BY user_id
	ORDER BY birthday DESC) AS total
    WHERE cum_sum <= 10;

-- Задание №4

SELECT IF ((
	SELECT count(posts_likes.like_type) 
	FROM posts_likes, profiles 
	WHERE posts_likes.user_id = profiles.user_id AND profiles.gender = 'm') > 
(
	SELECT count(posts_likes.like_type) 
    FROM posts_likes, profiles 
    WHERE posts_likes.user_id = profiles.user_id AND profiles.gender = 'f'),
'MALE', 'FEMALE');

-- Задание № 5
SELECT id, SUM(count) AS sum_of_activities
	FROM(
		SELECT COUNT(id) AS count, from_user_id AS id FROM messages GROUP BY from_user_id -- количество сообщений
		UNION ALL
		SELECT COUNT(id) AS count, user_id AS id from posts GROUP BY user_id -- количество постов
		UNION ALL
		SELECT COUNT(like_type) AS count, user_id AS id from posts_likes GROUP BY user_id -- количество лайков
		UNION ALL
		SELECT COUNT(id) AS count, user_id AS id from media GROUP BY user_id -- количество отправленных медиафайлов
		UNION ALL
		SELECT COUNT(from_user_id) AS count, to_user_id AS id FROM friend_requests AS to_fr WHERE request_type = 1 GROUP BY to_user_id -- количество друзей 1
		UNION ALL
		SELECT COUNT(to_user_id) AS count, from_user_id AS id FROM friend_requests AS from_fr WHERE request_type = 1 GROUP BY from_user_id -- количество друзей 2
     UNION ALL
     SELECT COUNT(id) AS count, id FROM users GROUP BY id -- добавим id юзеров, которые не произвели никаких действий. У таких юзеров поле count буде равно 1.
	) AS t 
GROUP BY id
ORDER BY SUM(count) DESC -- сумма всех активностей
LIMIT 10; 
USE notes_bot;


-- Вывести всех информацию обо всех, кто писал боту.

SELECT first_name, last_name, telegram_id, 1 as is_in_users FROM users
UNION
SELECT first_name, last_name, telegram_id, 0 as is_in_users FROM unknown_members;

-- Вывести количество людей, включенных в проект.

SELECT count(project_members.user_id) as count, projects.name 
FROM project_members
	JOIN projects ON project_members.project_id = projects.id
GROUP BY project_members.project_id
ORDER BY count DESC;
	

	

USE notes_bot;

-- Представление содержит таблицу админов бота, которые могут удалять проекты

CREATE OR REPLACE VIEW admins AS
	SELECT telegram_id, first_name, last_name 
    FROM users 	
    WHERE is_adm = true
WITH CHECK OPTION;

SELECT * FROM admins;

-- Представление содержит названия проектов и информацию о заметках. 

CREATE OR REPLACE VIEW projects_notes AS
	SELECT  p.name project, n.id note_id, n.file_name, n.updated_at edited 
    FROM notes n
		JOIN projects p ON p.id = n.project_id
	ORDER by n.project_id
WITH CHECK OPTION;
    
SELECT * FROM projects_notes;
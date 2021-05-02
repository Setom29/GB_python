def person_info(name, surname, y_of_birth, city, email, tel):
    """Функция выводит данные о пользователе в одну строку

    Именные переменные:
    name -- имя
    surname -- фамилия
    y_of_birth -- год рождения
    city -- город проживания
    email -- email пользователя
    tel -- телефон

    """
    person_dict = {'Имя': name, 'Фамилия': surname, 'Год рождения': y_of_birth,
                   'Город проживания': city, 'email': email, 'Телефон': tel}
    for item in person_dict.values():
        print(item, end=' ')


person_info(name='Ivan', surname='Ivanov', y_of_birth=1901,
            city='Moscow', email='ivanivanov@ivan.ru', tel='+71234567890')

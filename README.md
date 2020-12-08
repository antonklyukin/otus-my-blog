# otus-my-blog

$ pytest -v test/test_db_ex_04.py

Упраженение 4
=============

Создание моделей данных для сайта «Мой блог» на выбранную тему
--------------------------------------------------------------
Цель: В этой самостоятельной работе тренируем умения:
1. Создавать модели данных
2. Создавать связи между моделями
3. Работать с сессией
4. Делать простые запросы
Смысл:
Для того чтобы работать с SQLAlchemy в проектах с базой данных. Понимать как работать с ORM
Создать модели Post, Tag для сайта «Мой блог» на тему (ваша тема). Для пользователя можно использовать стандартную модель User.
Установить связи между моделями. Добавить некоторые данные.
Выбрать все посты конкретного пользователя с 2-мя любыми тегами
1. Создать новый проект «Мой блог», по нему будет 3 домашних задания. Рекомендуется создать для этого проекта отдельный репозиторий
2. Придумать тему блога. Она может быть любая какая вам более интересна (например экзотические птицы, занятия workout-ом, искусство, ...)
3. С помощью SQLAlchemy создать модели данных для блога, например (Post, User, ...) и все другие, которые вы считаете важными
4. Установить связи между моделями
5. В качестве примера ввести некоторые данные
6. Выбрать все посты конкретного пользователя, попробовать сделать другие запросы (Рекомендуется сделать это в виде тестов pytest, можно просто с помощью print)
7. Сдать ДЗ в виде ссылки на репозиторий.
Критерии оценки: Задание считается выполненным, когда:
Создана модель данных, в ней есть хотя бы один класс.

База заполняется данными через ORM
5 баллов

Дополнительно:
Есть пример запроса на выборку данных из базы (через ORM) (3 баллов)
Проверки реализованы в виде тестов на pytest (2 балла)

Итого 5 + 3 + 2 = максимально 10 баллов 

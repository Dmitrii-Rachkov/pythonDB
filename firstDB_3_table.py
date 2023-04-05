# Создание таблицы

import psycopg2

# Для создания таблицы в PostgreSQL применяется инструкция CREATE TABLE.
# Например, в вышесозданной базе данных "metanit" создадим таблицу people:

conn = psycopg2.connect(dbname="metanit", user="postgres", password="12PostgreSQL05", host="localhost")
cursor = conn.cursor()

# создаем таблицу people
cursor.execute("CREATE TABLE people (id SERIAL PRIMARY KEY, name VARCHAR(50),  age INTEGER)")

# поддверждаем транзакцию
conn.commit()
print("People table successfully created")

cursor.close()
conn.close()

# В метод cursor.execute() передается инструкция CREATE TABLE, которая создает таблицу people
# с тремя столбцами. Столбец id представляет идентификатор пользователя, хранит данные типа Serial,
# то есть число, которое будет автоматически генерироваться и инкрементироваться с каждой новой строкой
# и которое представляет первичный ключ. Второй столбец - name представляет строку - имя пользователя.
# И третий столбец - age представляет возраст пользователя.
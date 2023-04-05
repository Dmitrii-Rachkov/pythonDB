import psycopg2

# Для получения данных применяется SQL-команда SELECT.
# После выполнения этой команды курсор получает данные, которые можно получить
# с помощью одного из методов:
# fetchall() (возвращает список со всеми строками),
# fetchmany() (возвращает указанное количество строк)
# fetchone() (возвращает одну в наборе строку)

conn = psycopg2.connect(dbname="metanit", user="postgres", password="12PostgreSQL05",
                        host="localhost", port="5432")
cursor = conn.cursor()

# Например, получим все ранее добавленные данные из таблицы people:
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())

print("\n")


# При необходимости мы можем перебрать список, используя стандартные циклические конструкции:
cursor.execute("SELECT * FROM people")
for person in cursor.fetchall():
    print(f"{person[1]} - {person[2]}")

print("\n")

# Стоит отметить, что в примере выше необязательно вызывать метод fetchall,
# мы можем перебрать курсор в цикле как обычный набор:
cursor.execute("SELECT * FROM people")
for person in cursor:
    print(f"{person[1]} - {person[2]}")

print("\n")

# Получение части строк с помощью метода fetchmany(), в который передается количество строк:
cursor.execute("SELECT * FROM people")
# извлекаем первые 2 строки в полученном наборе
print(cursor.fetchmany(2))

print("\n")

# Выполнение этого метода извлекает следующие ранее неизвлеченные строки:
cursor.execute("SELECT * FROM people")
# извлекаем первые 2 строки в полученном наборе
print(cursor.fetchmany(2))
# извлекаем следующие 2 строки в полученном наборе
print(cursor.fetchmany(2))

print("\n")

# Метод fetchone() извлекает следующую строку в виде кортежа значений и возвращает его.
# Если строк больше нет, то возвращает None:
cursor.execute("SELECT * FROM people")
# извлекаем одну строку
print(cursor.fetchone())

print("\n")


# Данный метод удобно применять, когда нам надо извлечь из базы данных только один объект:
cursor.execute("SELECT name, age FROM people WHERE id=2")
# раскладываем кортеж на две переменных
name, age = cursor.fetchone()
print(f"Name: {name}\nAge: {age}")

cursor.close()
conn.close()


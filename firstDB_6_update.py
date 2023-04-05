import psycopg2


conn = psycopg2.connect(dbname="metanit", user="postgres", password="12PostgreSQL05",
                        host="localhost", port="5432")
cursor = conn.cursor()

# Для обновления в SQL выполняется команда UPDATE.
# Например, заменим у всех пользователей имя с Tom на Tomas:
cursor.execute("UPDATE people SET name='Tomas' WHERE name='Tom'")

# вариант с параметрами
# cursor.execute("UPDATE people SET name =%s WHERE name=%s", ("Tomas", "Tom"))

# Для выполнения обновления также надо выполнять метод conn.commit()
conn.commit()

# проверяем
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())


# Для множественного обновления, как и для множественного добавления, применяется метод executemany():
people = [(15, "Sam"), (18, "Alice")]
cursor.executemany("UPDATE people SET age=%s WHERE name=%s", people)
conn.commit()

# проверяем
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())

cursor.close()
conn.close()


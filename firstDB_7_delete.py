import psycopg2


conn = psycopg2.connect(dbname="metanit", user="postgres", password="12PostgreSQL05",
                        host="localhost", port="5432")
cursor = conn.cursor()

# Для удаления в SQL выполняется команда DЕLETE. Например, удалим всех пользователей с именем Sam:
cursor.execute("DELETE FROM people WHERE name=%s", ("Sam",))
conn.commit()

# проверяем
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())

# Множественное удаление:
# удаляем строки с id =1 и id=3
people = [(1,), (3,)]
cursor.executemany("DELETE FROM people WHERE id=%s", people)
conn.commit()

# проверяем
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())

cursor.close()
conn.close()


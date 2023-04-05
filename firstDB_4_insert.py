import psycopg2

conn = psycopg2.connect(dbname="metanit", user="postgres", password="12PostgreSQL05",
                        host="localhost", port="5432")
cursor = conn.cursor()

# добавляем строку в таблицу people
cursor.execute("INSERT INTO people (name, age) VALUES ('Tom', 38)")

# выполняем транзакцию
conn.commit()
print("Data added")

cursor.close()
conn.close()

# С помощью второго параметра в метод execute() можно передать значения для параметров SQL-запроса:
# bob = ("Bob", 42)
# cursor.execute("INSERT INTO people (name, age) VALUES (%s, %s)", bob)

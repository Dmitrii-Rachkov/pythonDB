import psycopg2

# Конструкция для автозаполнения кода
import psycopg2.extras

conn = psycopg2.connect(dbname="metanit", user="postgres", password="12PostgreSQL05",
                        host="localhost", port="5432")

# Чтобы включить автозаполнение кода нужна следующая конструкция:
cursor = conn.cursor()  # type: psycopg2.extras.DictCursor

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

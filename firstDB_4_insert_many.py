import psycopg2
# Конструкция для автозаполнения кода
import psycopg2.extras


conn = psycopg2.connect(dbname="metanit", user="postgres", password="12PostgreSQL05",
                        host="localhost", port="5432")

# Чтобы включить автозаполнение кода нужна следующая конструкция:
cursor = conn.cursor()  # type: psycopg2.extras.DictCursor

# Метод executemany() позволяет вставить набор строк:
people = [("Sam", 28), ("Alice", 33), ("Kate", 25)]
cursor.executemany("INSERT INTO people (name, age) VALUES (%s, %s)", people)

# выполняем транзакцию
conn.commit()
print("Data added")
cursor.close()
conn.close()




import psycopg2

conn = psycopg2.connect(dbname="metanit", user="postgres", password="12PostgreSQL05",
                        host="localhost", port="5432")
cursor = conn.cursor()

# Метод executemany() позволяет вставить набор строк:
people = [("Sam", 28), ("Alice", 33), ("Kate", 25)]
cursor.executemany("INSERT INTO people (name, age) VALUES (%s, %s)", people)

# выполняем транзакцию
conn.commit()
print("Data added")

cursor.close()
conn.close()


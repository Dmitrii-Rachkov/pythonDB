# Создание базы данных

import psycopg2

# Для создания базы данных применяется SQL-команда CREATE DATABASE, которой передается имя базы данных.
# Например, создадим базу данных с именем "metanit":

conn = psycopg2.connect(dbname="postgres", user="postgres", password="12PostgreSQL05",
                        host="localhost", port="5432")
cursor = conn.cursor()

# Обратите внимание, что для выражения "CREATE DATABASE" необходимо установиить автокоммит:
# Благодаря этому команда SQL, во-первых, выполняется немедленно.
# А во-вторых, выполняется вне транзакции
# (выражение "CREATE DATABASE" должно выполняться именно вне транзакции)

conn.autocommit = True


# команда для создания базы данных metanit
sql = "CREATE DATABASE metanit"

# выполняем код sql
cursor.execute(sql)
print("Database created successfully")

cursor.close()
conn.close()





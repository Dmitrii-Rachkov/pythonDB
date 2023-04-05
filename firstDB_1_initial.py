# Импортируем библиотеку для работы с базлй данных
import psycopg2

# Подключаемся к базе данных
conn = psycopg2.connect(dbname="testDB", host="localhost", user="postgres",
                 password="12PostgreSQL05", port="5432")
print("Connection successful")

# close(): закрывает подключение
# cursor(): возвращает объект cursor для осуществления запросов к бд
# commit(): поддверждает транзакцию
# rollback(): откатывает транзакцию

conn.close()

# execute(query, vars=None): выполняет одну SQL-инструкцию. Через второй параметр в код SQL можно
# передать набор параметров в виде списка или словаря

# executemany(query, vars_list): выполняет параметризованное SQL-инструкцию. Через второй параметр
# принимает наборы значений, которые передаются в выполняемый код SQL.

# callproc(procname[, parameters]): выполняет хранимую функцию. Через второй параметр можно передать
# набор параметров в виде списка или словаря

# mogrify(operation[, parameters]): возвращает код запроса SQL после привязки параметров

# fetchone(): возвращает следующую строку из полученного из БД набора строк в виде кортежа.
# Если строк в наборе нет, то возвращает None

# fetchmany([size=cursor.arraysize]): возвращает набор строк в виде списка.
# количество возвращаемых строк передается через параметр. Если больше строк нет в наборе,
# то возвращается пустой список.

# fetchall(): возвращает все (оставшиеся) строки в виде списка. При отсутствии строк
# возвращается пустой список.
# scroll(value[, mode='relative']): перемещает курсор в наборе на позицию value
# в соответствии с режимом mode.

# Перед выполнением первой команды SQL автоматически создается транзакция, в процессе которой можно
# выполнять различные выражения SQL с помощью методов execute/executemany курсора,
# но для подтверждения их выполнения необходимо вызывать метод commit() объекта connection.
# Условно это может выглядеть так:

cursor = conn.cursor()
cursor.execute(sql1)
conn.commit()
cursor.close()
conn.close()

# Если же надо, чтобы выражения sql автоматически выполнялись при каждом вызове метода cursor.execute(),
# то можно установить автокоммит с помощью свойства connection.autocommit:

conn.autocommit = True  # устанавливаем актокоммит
cursor = conn.cursor()
cursor.execute(sql1)  # непосредственное выполнение команды sql1
cursor.close()
conn.close()
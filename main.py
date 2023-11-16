import sqlite3
import xlrd

# Открываем файл Excel (.xls)
workbook = xlrd.open_workbook('Batteries.xls')

# Выбираем активный лист
sheet = workbook.sheet_by_index(0)

# Подключение к базе данных (в примере используется SQLite)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Создание таблицы в базе данных (если необходимо)
cursor.execute('''CREATE TABLE IF NOT EXISTS your_table
                (column1 TEXT, column2 TEXT, column3 INTEGER)''')

# Запись данных в базу данных
for row_num in range(1, sheet.nrows):  # Предполагается, что заголовки находятся в первой строке
    row = sheet.row_values(row_num)

    # Check the length of the row
    if len(row) != 3:
        print("Unexpected number of values in row {}: {}".format(row_num, len(row)))
        continue  # Skip this row or handle it differently if needed

    # Unpack values if the row has the expected number of values
    column1, column2, column3 = row
    cursor.execute("INSERT INTO your_table VALUES (?, ?, ?)", (column1, column2, column3))

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()


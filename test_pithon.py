import os
import xlrd
import database as db
#
# folder_path = r'D:\google table\2023 Electrics & Electronics'
#
# items = os.listdir(folder_path)
#
# for item in items:
#     print(item)


# Открываем таблицы -->
book = xlrd.open_workbook("Batteries.xls")
# Сколько страниц в xls таблицие -->
print(f"Страниц в xls таблице - {book.nsheets}")
# Имя страниц таблицы -->
print(f"Worksheet name(s): {book.sheet_names()}")
# Берем 1 страницу используем индексы для выбора страниц -->
sh = book.sheet_by_index(0)
# Вывод Имени страницы Кол-во Строк Кол-во Колонок -->
print(f"Info - {book.sheet_by_index(0).name}\nСтроки - {sh.nrows}\nКолонки - {sh.ncols}")
info = sh.row(1)

for i in range(len(info)):
    info[i] = str(info[i].value).replace('text:', '').strip()

db.add_company(*info)



# print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
# for rx in range(sh.nrows):
#     print(sh.row(rx))
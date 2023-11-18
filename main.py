import os
import xlrd
import database as db
import logging

logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

folder_path = r'D:\google table'

items = os.listdir(folder_path)

for item in items:
    package = f'{folder_path}/{item}'
    for i in package:
        file_path = f'{package}/{i}'
        print(file_path)
        # or use f-string (note the 'r' prefix for the raw string)
        # file_path = rf'D:\google table\2023 Electrics & Electronics\{item}'
        # Now you can use file_path as the full path to each item
    # # Открываем таблицы -->
    #     try:
    #         # Open the workbook
    #         book = xlrd.open_workbook(file_path)
    #
    #         # Get the first sheet
    #         sh = book.sheet_by_index(0)
    #
    #         for i in range(1, sh.nrows):
    #             info = sh.row(i)
    #             print(info)
    #
    #             for j in range(len(info)):
    #                 info[j] = str(info[j].value).replace('text:', '').strip()
    #                 print(info)
    #
    #             try:
    #                 db.add_company(*info)
    #             except Exception as e:
    #                 # Log the exception to the file
    #                 logging.error(f"Error processing file '{file_path}': {e}")
    #     except Exception as e:
    #         # Log the exception to the file
    #         logging.error(f"Error opening file '{file_path}': {e}")
    #





# Сколько страниц в xls таблицие -->
# print(f"Страниц в xls таблице - {book.nsheets}")t
# Имя страниц таблицы -->
# print(f"Worksheet name(s): {book.sheet_names()}")
# Вывод Имени страницы Кол-во Строк Кол-во Колонок -->
# print(f"Info - {book.sheet_by_index(0).name}\nСтроки - {sh.nrows}\nКолонки - {sh.ncols}")
#
# print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
# for rx in range(sh.nrows):
#     print(sh.row(rx))
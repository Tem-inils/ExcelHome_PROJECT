import sqlite3

connection = sqlite3.connect('test_db.db')

sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS info_xls (cmp_name TEXT, prov_name TEXT, city_name TEXT) ')
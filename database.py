import sqlite3

db = sqlite3.connect('test.db')

sql = db.cursor()

sql.execute(
    'CREATE TABLE IF NOT EXISTS info_xls (id INTEGER PRIMARY KEY AUTOINCREMENT, Company_Name TEXT, Province TEXT, City TEXT, Contact_Person TEXT, Mr_Ms TEXT, Mobile_Phone TEXT, Tel TEXT, Fax TEXT, Address TEXT, Post_Code TEXT, Website TEXT, Introduction TEXT, Main_Products TEXT, Company_NameCHINE TEXT);')

db.close()


def add_company(cpm_name=None, province=None, city=None, contact_person=None, mr_ms=None, mobile_phone=None, tel=None, fax=None, address=None, post_code=None, website=None,
                introduction=None, main_products=None, company_name_chine=None):

    db = sqlite3.connect('your_database.db')

    sql = db.cursor()

    sql.execute(
        'INSERT INTO info_xls (Company_Name, Province, City, Contact_Person, Mr_Ms, Mobile_Phone, Tel, Fax, Address, Post_Code, Website, Introduction, Main_Products, Company_NameCHINE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',
        (cpm_name, province, city, contact_person, mr_ms, mobile_phone, tel, fax, address, post_code, website,
         introduction, main_products, company_name_chine))

    db.commit()



import xlrd
import datetime as db


filename = 'Batteries.xls'

wb = xlrd.open_workbook(filename)

wshhet = wb.sheet_by_index(0)

company_names = []
# print(wshhet.nrows - вниз)


for i in range(1, wshhet.nrows):
    cmp_name = wshhet.cell_value(i, 0)
    company_names.append(cmp_name)



print(company_names)
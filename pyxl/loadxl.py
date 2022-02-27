import openpyxl

save_path = 'pyxl/users02.xlsx'

wb = openpyxl.load_workbook(save_path)

ws = wb.active

ws['A1'] = 1

ws.append(['2030-01-03', '기계식 키보드',1200, 15])

wb.save(save_path)
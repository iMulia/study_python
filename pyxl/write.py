import openpyxl

save_path = '../pyxl study/users01.xlsx'

wb = openpyxl.load_workbook(save_path)

ws = wb.active

ws['A1'] = '날짜'


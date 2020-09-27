from openpyxl import load_workbook, Workbook

# წაიკითხა F5 ფანჯარა
wb = load_workbook(filename = 'empty_book.xlsx')
sheet_ranges = wb['Pi']
tmp = sheet_ranges['F5'].value
wb.close()


#ჩაწერა

wb = Workbook()
secondFile = 'Copied-here.xlsx'
ws = wb.active
var = ''
var += 'A'
var += '4'
print(var)
ws[f'{var}'] = tmp

wb.save(filename=secondFile)
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Hello, World!"
print(wb.sheetnames)
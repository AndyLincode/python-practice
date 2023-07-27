from openpyxl import Workbook
import csv

data_rows = [fields for fields in csv.reader(open('file.csv', newline=""))]
print(data_rows)

wb = Workbook()
ws = wb.active
ws.title = "my_file"
ws.sheet_properties.tabColor = '1B4658'
for row in data_rows:
    ws.append(row)

wb.save("MyFile.xlsx")

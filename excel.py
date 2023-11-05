import openpyxl
workbook = openpyxl.Workbook()
worksheet = workbook.active

text_data = [
    ['Name', 'Age'],
    ['Arnab', 21],
    ['Alice', 25],
    ['Bob', 35],
]

for row in text_data:
    worksheet.append(row)

workbook.save('./xl_data/test_data.xlsx')
print('Excel file saved successfully.')

workbook = openpyxl.load_workbook('./xl_data/test_data.xlsx')
worksheet = workbook['Sheet']

for row in worksheet.iter_rows(values_only=True):
    for cell in row:
        print(cell, end='\t')
    print()

workbook.close()

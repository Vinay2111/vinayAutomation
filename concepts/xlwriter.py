import openpyxl

workbook=openpyxl.load_workbook("../excel/testdata.xlsx")
sheet=workbook["login"]

sheet.cell(row=4,column=5).value="age"

workbook.save("..//excel//testdata.xlsx")
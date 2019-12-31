import xlwings as xw

wb = xw.Book()
ws = wb.sheets["Sheet1"]
ws.range("A1").value = [[1], [2], [3], [4], [5]]
ws.range("A2").value = [2, 2, 3]
wb.save(r"test.xlsx")
wb.close()

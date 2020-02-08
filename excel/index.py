import xlwings as xw

wb = xw.Book()
# 打开现有的工作簿
# app = xw.App(visible=False, add_book=False)
# wb = app.books.open('test.xlsx')
sheet = wb.sheets["Sheet1"]
# 设置一维数据（一行）
sheet.range("A1").value = ["项目名称", "在线地址"]
# 设置二维数据（n行n列）
sheet.range("A2").value = [
    ["倾城之链", "https://nicelinks.site"],
    ["Arya - 在线 Markdown 编辑器", "https://markdown.lovejade.cn"],
    ["ARYA JARVIS DOC", "https://arya.lovejade.cn"],
    ["晚晴幽草轩", "https://jeffjade.com"],
    ["静晴轩别苑", "https://nice.lovejade.cn"],
    ["天意人间舫", "https://blog.lovejade.cn"],
    ["静轩之别苑", "https://quickapp.lovejade.cn"],
]
# 自动调整单元格大小；注：此方法是在单元格写入内容后，再使用，才有效
sheet.autofit()
# 设置背景色
sheet.range("A1:V3").color = (200, 200, 200)
# 保存 Excel
wb.save(r"test.xlsx")
wb.close()

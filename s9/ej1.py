from openpyxl import Workbook
wb=Workbook()
ws=wb.active
ws.title="Datos"
wb.save("mi_libro.xlsx")
from openpyxl import load_workbook
wb=load_workbook(filename="Ventas.xlsx")
ws=wb["Ventas"]
for fila in ws.rows:
    if fila[0].value=="Manzanas":
        fila[2].value="0.55"
wb.save("Ventas.xlsx")
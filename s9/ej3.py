
from openpyxl import load_workbook
wb=load_workbook(filename="Ventas.xlsx")
ws=wb["Ventas"]
datos=[]
for fila in ws.rows:
    fd=[]
    for celdas in fila:
        fd.append(celdas.value)
    datos.append(fd)
for i, fila in enumerate(datos):
    print(f"Filas{i+1},{fila}")
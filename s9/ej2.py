from openpyxl import Workbook
datos=[
    ["Productos","Cantidad","Precio"],
    ["Manzanas",50,0.5],
    ["Naranjas",30,0.75]
]
wb=Workbook()
ws=wb.active
ws.title="Ventas"
for i, filas in enumerate(datos):
    for j,valor in enumerate(filas):
        ws.cell(row=i+1,column=j+1,value=valor)
wb.save("Ventas.xlsx")




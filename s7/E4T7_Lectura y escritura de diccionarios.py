estudiantes={}
archivo=open("datosnombres.txt","r")
lineas=archivo.readlines()
archivo.close()

for linea in lineas:
    datos=linea.strip().split(",")
    nombre=datos[0]
    edad=int(datos[1])
    calificaciones=[int(x) for x in datos[2:]]
    estudiantes[nombre]={ "edad":edad,
    "calificaciones":calificaciones}
    archivo.close()
print(estudiantes)


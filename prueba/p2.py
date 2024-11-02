"""
#problema 1 con with
nombres=["Ana","Juan","Maria","Pedro","Juancho"]
archivo="nombres2.txt"
with open(archivo,"w") as f:
    for nombre in nombres:
        f.write(nombre +"/n")


#problema 1 sin with
nombres=["Ana","Juan","Maria","Pedro","Juancho"]
archivo="nombres3.txt"
f=open(archivo,"w")
for nombre in nombres:
    f.write()

#problema 2
archivo="nombres.txt"
nombres=[]
f=open(archivo,"r")
for linea in f:
    nombre=linea.s
    trip()
    nombres.append(nombre)
f.close()
print(nombres)

"""



archivo=open("numerosenteros.txt","r")
lista=[]
for linea in archivo:
    lista.append(linea.strip())
num=[int(x) for x in lista]
s=sum(num)
print(s)
archivo.close()
archivo=open("nombres.txt","r")
lista=[]
for linea in archivo:
    lista.append(linea.strip())
print(lista)
archivo.close()
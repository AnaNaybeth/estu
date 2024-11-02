lista=["Carlos","Ramon","Sofia","Jorge","Maria","Helena"]
arch="nombres.txt"

arch2=open(arch,"w")
for nombre in lista:
    arch2.write(nombre+"\n")
arch2.close()

"""
#Problema1
from fractions import Fraction
f1=Fraction(1,2)
f2=Fraction(1,3)
suma=f1+f2
print(f"suma:{suma}")
mult=f1*f2
print(f"multiplicacion:{mult}")

#problema2
c1=complex(3,4)
c2=complex(2,1)

suma=c1+c1
print(f"suma:{suma}")
resta=c1-c2
print(f"resta:{resta}")

#problema3
import statistics
numeros=[]
for i in range(25):
    numero=int(input(f"ingrese el numero{i+1}:"))
    numeros.append(numero)
mediana=statistics.median(numeros)
moda=statistics.mode(numeros)
media=statistics.mean(numeros)
print(f"media{media},mediana{mediana},moda{moda}")


#Problema 4
import sympy as sp
x=sp.symbols("x")
f=x**2+3*x+2
limite=float(input("ingrese el limite:"))
lim=sp.limit(f,x,limite)
derivada=sp.diff(f,x)
print(f"Limite:{lim} Derivada:{derivada}")


#problema 5
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,3,5,7,11]
plt.scatter(x,y,color="red")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.title("Grafica de puntos")
plt.show()


#problema 6
import matplotlib.pyplot as plt
categoria=["A","B","C","D"]
valores=[10,20,15,25]
plt.bar(categoria,valores,color="blue")
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.title("Grafica de barras")
plt.show()


#problema 7
import matplotlib.pyplot as plt
categoria=["A","B","C","D"]
valor=[10,20,15,25]
plt.barh(categoria,valor,color="green")
plt.xlabel("Categorias")
plt.xlabel("Valores")
plt.title("Grafica de barras horizontal")
plt.show()
"""

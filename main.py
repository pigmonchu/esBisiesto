import mBisiesto

n = input("Año: ")

while not mBisiesto.esEntero(n) or mBisiesto.esBisiesto(int(n)):
    print(n, "incorrecto. Vuelve a intentar")
    n = input("Año: ")

print("Este sí,", n , "es bisiesto")
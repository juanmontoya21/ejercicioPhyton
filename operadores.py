"""#operadores aritmeticos

numero1 = 2
numero2 = 5

print("suma:", numero1+numero2)
print("division: ", numero1//numero2)
print("potenciacion: ", numero1**numero2)
print("residuo: ", numero1%numero2)

#operadores de comparacion: <,>,>=,<=,!=,==
dato1= int(input("ingrese el primer numero: "))
dato2=int(input("ingrese el segundo numero: "))

if dato1>dato2:
    print(f"{dato1} es mayor")
else:
    print(f"{dato2} es mayor")

if dato1%2==0:
    print("es par")
else:
    print("es impar")

print(f"{dato1} es par " if dato1%2==0 else f"{dato1} es impar")"""

#title(), upper(), lower()
texto= "hola PERRO"

print(texto.title())
print(texto.upper())
print(texto.lower())


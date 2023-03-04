nombre = input("digite su nombre: ")
edad = int(input("digite su edad: "))

if edad<=17:
    print(f"{nombre} usted es menor de edad con {edad}")
else:
    print(f"{nombre} usted es mayor de edad con {edad}")
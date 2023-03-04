edad= int(input("ingrese su edad: "))
grupo = input("ingrese el grupo a l que pertenece sea adulto o infante: ")

if edad>=18 and grupo == "adulto":
    print("usted puede entrar")
elif edad<=17 and grupo == "adulto":
    print("no puedes ingresar al grupo eres menor de 18")
elif edad<=17 and grupo == "infante":
    print("usted puede ingresar cumple las condiciones")
else:
    print("esta opcion no es validad")
nombre = input("ingrese su nombre: ")
año_nacimiento = int(input("ingrese su año de nacimiento: "))
año_actual = int(input("ingrese el año actual: "))
if año_actual<año_nacimiento:
    print("el año nacimiento no puede ser mayor al año de actual")
else:
    print(f"{nombre} su edad es : {año_actual-año_nacimiento }")
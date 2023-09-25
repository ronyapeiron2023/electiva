edad = int(input("Ingresa tu edad: "))
if edad < 13:
    print("Eres un niño.")
elif edad < 20:
    print("Eres un adolescente.")
elif edad < 30:
    print("Eres un adulto joven.")
elif edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un anciano.")

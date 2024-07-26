print ("Ingresa tu nota, segun tu nota obtendras el rango de tu calificacion: ")

nota = input("Ingresa tu nota: ")
if nota >= 90:
    print("Calificación: A")
elif nota >= 80:
    print("Calificación: B")
elif nota >= 70:
    print("Calificación: C")
elif nota >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")



#convertir una cadena de texto en una lista

cadena = "monitor, teclado, mouse, pendrive" 
lista4 = cadena.split(", ")
print(lista4)

#contar elementos de una lista

print(len(lista4))


#lista de actividad marketing
clics = [120, 160, 180, 140, 200]
print("lista inicial:", clics)
print("clics del primer dia:", clics[0])
clics[1] = 150
print("Despues de modificar:",clics)
clics.append(220)
print("Despues de agregar:", clics)
clics.remove(180)
print("Despues de eliminar:", clics)

#tuplas

ubicaciones-geograficas = ("latitud", "longitud", "altitud")
print(ubicaciones-geograficas)

coordinates = (19.432608, -99.133209, 2240)
print(coordinates)

estadistica-media = (10, 20, 30, 40, 50)
print(estadistica-media)
datos-personales = ("cedula", "nombre", "apellido", "edad")
print(datos-personales)
#precio Helado - Joel Franco Muñoz

mensaje = """ 
Seleccione el helado de su preferencia: 
 1 - Helado con oreo
 2 - Helado con m&m
 3 - Helado con fresas
 4 - Helado con brownie

"""
print (mensaje)
opcion = input()

if opcion == "oreo" or "Oreo" or "OREO" or "1" :
    precio = 19
if opcion == "m&m" or "M&m" or "M&M" or "2" :
    precio = 25
if opcion == "fresas" or "Fresas" or "FRESAS" or "3" or "fresa" or "Fresa" or "FRESA" :
    precio = 22
if opcion == "brownie" or "Brownie" or "BROWNIE" or "4" :
    precio = 28

print("El costo total es ${}".format(precio))


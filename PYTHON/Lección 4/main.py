# lista = Ariel , Liliana , Osvaldo
nombres = ["Naty", "Osvaldo", "Romi" , "Lautaro"]
print(nombres)
# mostrar en el indice que se ecuentra el elemento en la lista
print(nombres[0])
print(nombres[2])
# muestra el último elemento de la lista
print(nombres[-1])

# recuperar un rango de nuestra lista
print(nombres[0:2])

# para ir del inicio de la lista al indice(sin incluirlo
print(nombres[ :3])

# desde el indice indicado hasta el final
print(nombres[1: ])

# Modificar un valor
nombres[1] = "Iris"
print(nombres)

# iterar nuestra lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print("se acaba los elementos de la lista")

# preguntamos cuantos elementos tiene
print(len(nombres))

# agregamos un elemento
nombres.append("Naira")
print(nombres)

# incertar un elemento en un indice especifico
nombres.insert(1,"Fernando")
print(nombres)
nombres.insert(3,"Jazmín")
print(nombres)

# Eliminar un elemento de la lista
nombres.remove("Naty")
print(nombres)

# Eliminar el último elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[3] # delete (iliminar)
print(nombres)

# Eliminar todos os elementos de la lista
nombres.clear()
print(nombres)



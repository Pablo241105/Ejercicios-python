#Listas en python
#Definicion e inicializacion

vNombres= []

#Insertar un dato
vNombres.insert(0,"Juan")
vNombres.insert(1,"Pepe")
vNombres.insert(2,"Ines")
vNombres.append("Minerva")
vNombres.insert(1,"Julian")

#Eliminar un elemento
vNombres.remove("Pepe")
print("El nombre borrado es",vNombres.pop(1))
#Ordenar una lista
vNombres.sort(reverse=True)
#Contar el numero de elementos



print("Aparece este numero de veces",vNombres.count("Pepe"))
print("La lista tiene",len(vNombres))


print((vNombres))
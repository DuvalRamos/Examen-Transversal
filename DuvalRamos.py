#DATOS

productos = {"01HPHD": ["HP", 14, "4GB", "DD", "100GB", "Intel Core i3", "Nvidia GTX1050"],
             "02HPHD": ["HP", 15, "6GB", "DD", "200GB", "Intel Core i3", "Nvidia GTX1150"],
             "03HPHD": ["HP", 16, "8GB", "SSD", "300GB", "Intel Core i5", "Nvidia GTX1250"],
             "04HPHD": ["HP", 17, "12GB", "SSD", "400GB", "Intel Core i5", "Nvidia GTX1350"],
             "05HPHD": ["HP", 18, "16GB", "SDD", "500GB", "Intel Core i7", "Nvidia GTX1450"],
             "01LEHD": ["LENOVO", 14, "4GB", "DD", "100GB", "Intel Core i3", "Nvidia GTX2050"],
             "02LEHD": ["LENOVO", 15, "6GB", "DD", "200GB", "Intel Core i3", "Nvidia GTX2150"],
             "03LEHD": ["LENOVO" ,16, "8GB", "SSD", "300GB", "Intel Core i5", "Nvidia GTX2250"],
             "04LEHD": ["LENOVO", 17, "12GB", "SSD", "400GB", "Intel Core i5", "Nvidia GTX2350"],
             "05LEHD": ["LENOVO", 18, "16GB", "SDD", "500GB", "Intel Core i7", "Nvidia GTX2450"],
             "01ASHD": ["ASUS", 14, "4GB", "DD", "100GB", "AMD Ryzen 3", "Nvidia GTX3050"],
             "02ASHD": ["ASUS", 15, "6GB", "DD", "200GB", "AMD Ryzen 3" "Nvidia GTX3150"],
             "03ASHD": ["ASUS", 16, "8GB", "SSD", "300GB", "AMD Ryzen 5", "Nvidia GTX3250"],
             "04ASHD": ["ASUS", 17, "12GB", "SSD", "400GB", "AMD Ryzen 5", "Nvidia GTX3350"],
             "05ASHD": ["ASUS", 18, "16GB", "SDD", "500GB", "AMD Ryzen 7", "Nvidia GTX3450"]}

stock = {"01HPHD": [199999, 5], 
        "02HPHD": [299999, 7],
        "03HPHD": [399999, 9],
        "04HPHD": [499999, 11],
        "05HPHD": [599999, 13],
        "01LEHD": [199999, 6],
        "02LEHD": [299999, 8],
        "03LEHD": [399999, 10],
        "04LEHD": [499999, 12],
        "05LEHD": [599999, 14],
        "01ASHD": [199999, 4],
        "02ASHD": [299999, 3],
        "03ASHD": [399999, 2],
        "04ASHD": [499999, 1],
        "05ASHD": [599999, 21]}

#FUNCIONES

def stock_marca(marca):
    retorno = 0
    if marca in "HP" or marca in "hp" or marca in "Hp":
        cantidad = stock["01HPHD"][1]
        retorno = retorno + cantidad
        cantidad = stock["02HPHD"][1]
        retorno = retorno + cantidad
        cantidad = stock["03HPHD"][1]
        retorno = retorno + cantidad
        cantidad = stock["04HPHD"][1]
        retorno = retorno + cantidad
        cantidad = stock["05HPHD"][1]
        retorno = retorno + cantidad
        return retorno
    elif marca in "LENOVO" or marca in "lenovo" or marca in "Lenovo":
        cantidad = stock["01LEHD"][1]
        retorno = retorno + cantidad
        cantidad = stock["02LEHD"][1]
        retorno = retorno + cantidad
        cantidad = stock["03LEHD"][1]
        retorno = retorno + cantidad
        cantidad = stock["04LEHD"][1]
        retorno = retorno + cantidad
        cantidad = stock["05LEHD"][1]
        retorno = retorno + cantidad
        return retorno
    elif marca in "ASUS" or marca in "asus" or marca in "Asus":
        cantidad = stock["01ASHD"][1]
        retorno = retorno + cantidad
        cantidad = stock["02ASHD"][1]
        retorno = retorno + cantidad
        cantidad = stock["03ASHD"][1]
        retorno = retorno + cantidad
        cantidad = stock["04ASHD"][1]
        retorno = retorno + cantidad
        cantidad = stock["05ASHD"][1]
        retorno = retorno + cantidad
        return retorno
    else:
        print("Marca no encontrada")

def busqueda_precio(p_min, p_max):
    resultados = []
    if p_min > 599999 or p_max < 199999:
        print("No hay notebooks en ese rango de precio")
    else:
        consulta = stock["01HPHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("HP--01HPHD")
        consulta = stock["02HPHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("HP--02HPHD")
        consulta = stock["03HPHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("HP--03HPHD")
        consulta = stock["04HPHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("HP--04HPHD")
        consulta = stock["05HPHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("HP--05HPHD")
        consulta = stock["01LEHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("Lenovo--01LEHD")
        consulta = stock["02LEHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("Lenovo--02LEHD")
        consulta = stock["03LEHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("Lenovo--03LEHD")
        consulta = stock["04LEHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("Lenovo--04LEHD")
        consulta = stock["05LEHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("Lenovo--05LEHD")
        consulta = stock["01ASHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("Asus--01ASHD")
        consulta = stock["02ASHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("Asus--02ASHD")
        consulta = stock["03ASHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("Asus--03ASHD")
        consulta = stock["04ASHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("Asus--04ASHD")
        consulta = stock["05ASHD"][0]
        if consulta >= p_min and consulta <= p_max:
            resultados.append("Asus--05ASHD")
        return resultados
      
def actualizar_precio(modelo, p):
    if modelo in "01HPHD":
        stock["01HPHD"][0] = p
        return True
    elif modelo in "02HPHD":
        stock["02HPHD"][0] = p
        return True
    elif modelo in "03HPHD":
        stock["03HPHD"][0] = p
        return True
    elif modelo in "04HPHD":
        stock["04HPHD"][0] = p
        return True
    elif modelo in "05HPHD":
        stock["05HPHD"][0] = p
        return True
    elif modelo in "01LEHD":
        stock["01LEHD"][0] = p
        return True
    elif modelo in "02LEHD":
        stock["02LEHD"][0] = p
        return True
    elif modelo in "03LEHD":
        stock["03LEHD"][0] = p
        return True
    elif modelo in "04LEHD":
        stock["04LEHD"][0] = p
        return True
    elif modelo in "05LEHD":
        stock["05LEHD"][0] = p
        return True
    elif modelo in "01ASHD":
        stock["01ASHD"][0] = p
        return True
    elif modelo in "02ASHD":
        stock["02ASHD"][0] = p
        return True
    elif modelo in "03ASHD":
        stock["03ASHD"][0] = p
        return True
    elif modelo in "04ASHD":
        stock["04ASHD"][0] = p
        return True
    elif modelo in "05ASHD":
        stock["05ASHD"][0] = p
        return True
    else: return False
    

#CODIGO MAIN

contador = 0
while contador == 0:
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")

    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion < 0 or opcion > 4:
            print("Debe seleccionar una opción valida!!!")
            print(" ")
        else:
            contador = 1
    except ValueError:
        print("Debe ingresar una opción valida!!!")
        print(" ")

    if opcion == 1:
        marca = str(input("Ingrese marca a consultar: "))
        respuesta = stock_marca(marca)
        print("El stock es de:",respuesta)
        print(" ")
        contador = 0

    if opcion == 2:
        iterador = 0
        while iterador == 0:
            try:
                p_min = int(input("Ingrese precio minimo: "))
                p_max = int(input("Ingrese precio maximo: "))
                if p_min < 0 or p_max < 0:
                    print("Debe ingresar valores enteros positivos!!!")
                else:
                    iterador = 1
            except ValueError:
                print("Debe ingresar valores enteros!!!")
        respuesta = busqueda_precio(p_min, p_max)
        print("Los notebooks entre los precios consulta son:", respuesta)
        print(" ")
        contador = 0
    
    if opcion == 3:
        try:
            modelo = str(input("Ingrese el modelo a actualizar: "))
            precio = int(input("Ingrese precio nuevo: "))
            respuesta = actualizar_precio(modelo, precio)
            if respuesta is False:
                print("El modelo no existe!!!")
                print(" ")
            elif respuesta is True:
                print("Precio actualizado!!!")
                print(" ")
        except ValueError:
            print("Debe ingresar un precio valido!!! (Números enteros)")
            print(" ")
        contador = 0
    
    if opcion == 4:
        contador = 1
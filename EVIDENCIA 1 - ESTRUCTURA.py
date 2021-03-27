datos = []
mas = 1
codigo = 0
opcion = 0
goback = 1

while True:
    print("\n**MENU**\n")
    print("1 - Registrar una Venta")
    print("2 - Consultar una Venta")
    print("3 - Salir")
    
    opcion = input("Elige una opcion: ")
    
    if opcion == "1":
        codigo += 1
        mas = 1
        while mas == 1:
            descripcion = input("Descripcion del Artículo: ")
            cantidad = int(input("Cantidad de piezas vendidas: "))
            precio = float(input("Precio del Artículo: "))
            
            registro = list()
            registro.append(codigo)
            registro.append(descripcion)
            registro.append(cantidad)
            registro.append(precio)
            registro.append(cantidad * precio)
            datos.append(registro)
            total = 0
            for registro in datos:
                if registro[0]==codigo:
                    total += registro[4]
            mas =int(input("\n¿Deseas capturar otro artículo?\n(1-Si / 0-No): "))
            if mas == 0:
                print("\nSu total es: ", total, "\n")
            #goback = int(input("\n¿Deseas volver al MENÚ?\n(1-Si / 0-No): "))
    elif opcion == "2":
        print("\nConsultar Venta\n")
        codigo = int(input("\nDime qué codigo de venta deseas consultar: \n"))
        for registro in datos:
            if registro[codigo]:
                print(registro)
            else:
                print("Codigo de venta no valido.")
                goback = int(input("¿Deseas volver al MENÚ?\n(1-Si / 0-No): "))
    elif opcion == "3":
        print("\nGracias por utilizar el programa\n")
        break
    else:
        print("\nError, intente otra vez\n")
        goback = int(input("¿Deseas volver al MENÚ?\n(1-Si / 0-No): "))
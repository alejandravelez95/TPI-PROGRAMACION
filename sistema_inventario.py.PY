#Dentro de esta función se desarrollará el ingreso de herramientas nuevas al sistema de inventario
def cargar_herramientas(inventario):
    print("\n--- Carga de Herramientas ---")

    #Se crea una estructura repetitiva en verdadero
    while True:
        #Se pide ingresar la cantidad, se convierte el valor en tipo de dato númerico
        #Además, se evalua que la cantidad de herramientas no sean mayores a 0
        #Si se cumple, se crea un raise para evitar que se rompa el programa y ademas
        #Se genera una excepcion.
        try:
            cantidad_str = input("Ingrese cuántas herramientas distintas desea cargar: ")
            cant_herramientas = int(cantidad_str)
            if cant_herramientas <= 0:
                raise ValueError("La cantidad de herramientas a cargar debe ser mayor a 0.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    #Se crea una estructura repetitiva que se ejecutará la cantidad de veces que se indicó anteriormente
    for i in range(cant_herramientas):
        print(f"\nHerramienta {i + 1} de {cant_herramientas}:")
        
        #Se inicializa una variable como vacía para controlar el estado de la validación del nombre
        nombre_valido = None
        #Se crea una estructura repetitiva que continuará hasta que se obtenga un nombre correcto
        while nombre_valido is None:
            #Se pide ingresar el nombre, se eliminan los espacios extras al principio y al final
            #Además, se evalua que el nombre no esté vacío y que no exista en el inventario actual
            #Si alguna condición falla, se crea un raise para evitar que se rompa el programa y ademas
            #Se genera una excepcion.
            try:
                nombre_ingresado = input("Ingrese el nombre de la herramienta: ")
                nombre_limpio = nombre_ingresado.strip()
                if not nombre_limpio:
                    raise ValueError("El nombre de la herramienta no puede estar vacío.")
                for producto in inventario:
                    if producto['herramienta'].lower() == nombre_limpio.lower():
                        raise ValueError(f"La herramienta '{nombre_limpio}' ya existe en el inventario.")
                nombre_valido = nombre_limpio
            except ValueError as e:
                print(f"Error: {e}")

        #Se inicializa una variable como vacía para controlar el estado de la validación del stock
        stock_valido = None
        #Se crea una estructura repetitiva que continuará hasta que se obtenga un stock correcto
        while stock_valido is None:
            #Se pide ingresar el stock, se convierte el valor en tipo de dato númerico
            #Además, se evalua que la cantidad de stock no sea menor a 0
            #Si se cumple, se crea un raise para evitar que se rompa el programa y ademas
            #Se genera una excepcion.
            try:
                stock_str = input(f"Ingrese el stock inicial para '{nombre_valido}': ")
                stock = int(stock_str)
                if stock < 0:
                    raise ValueError("El stock inicial no puede ser negativo.")
                stock_valido = stock
            except ValueError as e:
                print(f"Error: {e}")

        #Se agrega el nuevo registro al inventario guardándolo en formato de diccionario
        inventario.append({'herramienta': nombre_valido, 'cantidad': stock_valido})
        print(f"¡Herramienta '{nombre_valido}' cargada con éxito!")



#Dentro de esta función se desarrollará la visualización del listado completo del inventario
def mostrar_inventario(inventario):
    """Opción 2: Muestra el listado completo del inventario."""
    print("\n--- Visualización de Inventario ---")
    
    #Se evalua que el inventario no se encuentre vacío para evitar mostrar datos inexistentes
    #Si se cumple, se muestra un mensaje de aviso y se corta la ejecución de la función
    if not inventario:
        print("Todavía no hay herramientas cargadas en el inventario.")
        return
        
    #Se imprimen los encabezados de la tabla con sus respectivos formatos de alineación
    print(f"{'Herramienta':<30} | {'Stock':<10}")
    print("-" * 43)
    
    #Se crea una estructura repetitiva que recorrerá cada uno de los productos guardados en el inventario
    for producto in inventario:
        #Se imprimen en pantalla los datos de la herramienta y su cantidad correspondiente
        print(f"{producto['herramienta']:<30} | {producto['cantidad']:<10}")



#Dentro de esta función se desarrollará la consulta del stock de una herramienta específica
def consultar_stock(inventario):
    """Opción 3: Consulta el stock de una herramienta específica."""
    print("\n--- Consulta de Stock ---")
    
    #Se evalua que el inventario no se encuentre vacío para evitar buscar datos inexistentes
    #Si se cumple, se muestra un mensaje de aviso y se corta la ejecución de la función
    if not inventario:
        print("Todavía no hay herramientas cargadas en el inventario.")
        return
    
    #Se pide ingresar el nombre de la herramienta, se eliminan los espacios extras al principio y al final
    #Además, se evalua que el nombre de la herramienta no esté vacío
    #Si se cumple, se crea un raise para evitar que se rompa el programa y ademas
    #Se genera una excepcion.
    nombre = input("Ingrese el nombre de la herramienta a consultar: ")
    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        raise ValueError("El nombre de la herramienta no puede estar vacío.")

    #Se inicializa una variable bandera en falso para controlar si el producto fue hallado
    encontrado = False
    
    #Se crea una estructura repetitiva que recorrerá cada uno de los productos guardados en el inventario
    for producto in inventario:
        #Se evalua si el nombre de la herramienta coincide con el ingresado sin importar mayúsculas o minúsculas
        #Si se cumple, se muestran sus datos, se cambia la bandera a verdadero y se corta el ciclo repetitivo
        if producto['herramienta'].lower() == nombre_limpio.lower():
            print(f"Herramienta encontrada: '{producto['herramienta']}' - Stock disponible: {producto['cantidad']} unidades.")
            encontrado = True
            break
    
    #Se evalua si la bandera continúa en falso tras finalizar la búsqueda en el inventario
    #Si se cumple, significa que no existe y se muestra un mensaje indicando que no se encuentra en el catálogo
    if not encontrado:
        print(f"La herramienta '{nombre_limpio}' no se encuentra en el catálogo.")



#Dentro de esta función se desarrollará el reporte de productos con stock en cero
def reporte_agotados(inventario):
    """Opción 4: Reporte de productos con stock en cero."""
    print("\n--- Reporte de Productos Agotados ---")
    
    #Se evalua que el inventario no se encuentre vacío para evitar buscar datos inexistentes
    #Si se cumple, se muestra un mensaje de aviso y se corta la ejecución de la función
    if not inventario:
        print("Todavía no hay herramientas cargadas en el inventario.")
        return

    #Se crea una lista filtrada que almacena únicamente los productos cuya cantidad sea igual a cero
    agotados = [p for p in inventario if p['cantidad'] == 0]
    
    #Se evalua si la lista de productos agotados se encuentra vacía
    #Si se cumple, se muestra un mensaje indicando que ninguna herramienta tiene stock cero
    if not agotados:
        print("Ninguna herramienta tiene stock cero (no hay productos agotados).")
    #Si no se cumple, se procede a mostrar el listado de las herramientas que se quedaron sin stock
    else:
        #Se imprimen los encabezados de la tabla con sus respectivos formatos de alineación
        print(f"{'Herramienta Agotada':<30} | {'Stock':<10}")
        print("-" * 43)
        #Se crea una estructura repetitiva que recorrerá cada uno de los productos filtrados como agotados
        for producto in agotados:
            #Se imprimen en pantalla los datos de la herramienta agotada y su cantidad correspondiente
            print(f"{producto['herramienta']:<30} | {producto['cantidad']:<10}")



#Dentro de esta función se desarrollará el alta de un nuevo producto en el sistema de inventario
def alta_producto(inventario):
    """Opción 5: Alta de un nuevo producto (los errores ascienden a main)."""
    print("\n--- Alta de Nuevo Producto ---")
    
    #Se pide ingresar el nombre de la nueva herramienta, se eliminan los espacios extras al principio y al final
    #Además, se evalua que el nombre de la herramienta no esté vacío
    #Si se cumple, se crea un raise para evitar que se rompa el programa y ademas
    #Se genera una excepcion.
    nombre = input("Ingrese el nombre de la nueva herramienta: ")
    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        raise ValueError("El nombre de la herramienta no puede estar vacío.")

    #Se crea una estructura repetitiva que recorrerá cada uno de los productos guardados en el inventario
    for producto in inventario:
        #Se evalua si la herramienta ya existe en el inventario actual sin importar mayúsculas o minúsculas
        #Si se cumple, se crea un raise para evitar que se rompa el programa y ademas
        #Se genera una excepcion.
        if producto['herramienta'].lower() == nombre_limpio.lower():
            raise ValueError(f"La herramienta '{nombre_limpio}' ya existe en el inventario.")

    #Se pide ingresar el stock, se convierte el valor en tipo de dato númerico
    #Además, se evalua que la cantidad de stock no sea menor a 0
    #Si se cumple, se crea un raise para evitar que se rompa el programa y ademas
    #Se genera una excepcion.
    stock_str = input(f"Ingrese el stock inicial para '{nombre_limpio}': ")
    stock = int(stock_str)
    if stock < 0:
        raise ValueError("El stock inicial no puede ser negativo.")

    #Se agrega el nuevo registro al inventario guardándolo en formato de diccionario
    inventario.append({'herramienta': nombre_limpio, 'cantidad': stock})
    print(f"¡Producto '{nombre_limpio}' dado de alta con éxito!")



#Dentro de esta función se desarrollará la actualización de stock por venta o ingreso de una herramienta
def actualizar_stock(inventario):
    """Opción 6: Actualización de stock por venta o ingreso."""
    print("\n--- Actualización de Stock (Venta / Ingreso) ---")
    
    #Se evalua que el inventario no se encuentre vacío para evitar modificar datos inexistentes
    #Si se cumple, se muestra un mensaje de aviso y se corta la ejecución de la función
    if not inventario:
        print("Todavía no hay herramientas cargadas en el inventario.")
        return

    #Se pide ingresar el nombre de la herramienta, se eliminan los espacios extras al principio y al final
    #Además, se evalua que el nombre de la herramienta no esté vacío
    #Si se cumple, se crea un raise para evitar que se rompa el programa y ademas
    #Se genera una excepcion.
    nombre = input("Ingrese el nombre de la herramienta: ")
    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        raise ValueError("El nombre de la herramienta no puede estar vacío.")

    #Se inicializa una variable como vacía para controlar si el producto fue hallado
    producto_encontrado = None
    
    #Se crea una estructura repetitiva que recorrerá cada uno de los productos guardados en el inventario
    for producto in inventario:
        #Se evalua si el nombre de la herramienta coincide con el ingresado sin importar mayúsculas o minúsculas
        #Si se cumple, se guarda el producto encontrado en la variable y se corta el ciclo repetitivo
        if producto['herramienta'].lower() == nombre_limpio.lower():
            producto_encontrado = producto
            break

    #Se evalua si la variable continúa vacía tras finalizar la búsqueda en el inventario
    #Si se cumple, significa que no existe, se muestra un mensaje de aviso y se corta la ejecución de la función
    if not producto_encontrado:
        print(f"La herramienta '{nombre_limpio}' no existe en el inventario.")
        return

    print("Seleccione el tipo de movimiento:")
    print("1. Venta")
    print("2. Ingreso")
    tipo_mov = input("Ingrese '1' o 'venta' para venta, '2' o 'ingreso' para ingreso: ").strip().lower()

    #Se evalua si el tipo de movimiento ingresado no se encuentra entre las opciones válidas
    #Si se cumple, se muestra un mensaje de error y se corta la ejecución de la función
    if tipo_mov not in ['1', '2', 'venta', 'ingreso']:
        print("Error: Tipo de movimiento inválido. Debe ser 'venta' o 'ingreso' (o 1 / 2).")
        return

    #Se pide ingresar las unidades, se convierte el valor en tipo de dato númerico
    #Además, se evalua que las unidades del movimiento no sean menores o iguales a 0
    #Si se cumple, se crea un raise para evitar que se rompa el programa y ademas
    #Se genera una excepcion.
    unidades_str = input("Ingrese las unidades del movimiento: ")
    unidades = int(unidades_str)
    if unidades <= 0:
        raise ValueError("Las unidades del movimiento deben ser mayores a 0.")

    #Se evalua si el tipo de movimiento seleccionado corresponde a una venta
    if tipo_mov in ['1', 'venta']:
        #Se evalua si la cantidad actual de la herramienta es menor a las unidades que se quieren vender
        #Si se cumple, se crea un raise para evitar que se rompa el programa y ademas
        #Se genera una excepcion.
        if producto_encontrado['cantidad'] < unidades:
            raise ValueError(f"Stock insuficiente. Stock actual: {producto_encontrado['cantidad']}, unidades solicitadas: {unidades}.")
        
        #Se descuentan las unidades vendidas del stock actual de la herramienta
        producto_encontrado['cantidad'] -= unidades
        print(f"Venta realizada con éxito. Nuevo stock de '{producto_encontrado['herramienta']}': {producto_encontrado['cantidad']}.")
    #Si no se cumple, significa que el tipo de movimiento corresponde a un ingreso de mercadería
    else:
        #Se suman las unidades ingresadas al stock actual de la herramienta
        producto_encontrado['cantidad'] += unidades
        print(f"Ingreso realizado con éxito. Nuevo stock de '{producto_encontrado['herramienta']}': {producto_encontrado['cantidad']}.")

#Dentro de esta función se desarrollará la gestión de la estructura de datos local y el menú interactivo
def main():
    """Función principal: gestiona la estructura de datos local y el menú interactivo."""
    #Se inicializa la lista vacía para almacenar el inventario y la variable de control de la opción en cero
    inventario = []
    opcion = 0
    
    #Se crea una estructura repetitiva que continuará ejecutándose hasta que se seleccione la opción de salir
    while opcion != 7:
        print("\n_______________________________________")
        print("    SISTEMA DE CONTROL DE INVENTARIO    ")
        print("__________________________________________")
        print("1. Carga de herramientas con existencias iniciales")
        print("2. Visualización de inventario")
        print("3. Consulta de stock")
        print("4. Reporte de agotados")
        print("5. Alta de nuevo producto")
        print("6. Actualización de stock (venta / ingreso)")
        print("7. Salir")
        print("______________________________________________")
        
        #Se pide ingresar la opción, se convierte el valor en tipo de dato númerico
        #Además, se evalua que la opción elegida se encuentre dentro del rango válido
        #Si no se cumple, se crea un raise para evitar que se rompa el programa y ademas
        #Se genera una excepcion.
        try:
            opcion_str = input("Seleccione una opción (1 a 7): ")
            opcion = int(opcion_str)
            
            #Se evalua qué opción numérica ingresó el usuario para ejecutar la función correspondiente
            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reporte_agotados(inventario)
            elif opcion == 5:
                alta_producto(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
            elif opcion == 7:
                print("Saliendo del sistema de inventario.")
            else:
                raise ValueError("Opción fuera de rango (debe ser entre 1 y 7).")
                
        except ValueError as e:
            print(f"Error: {e}")

#Se evalua si el archivo se está ejecutando como el programa principal para dar inicio a la función main
if __name__ == "__main__":
    main()

from Biblioteca import *
from Clases import *
from getpass import *

registro = RegistroUsuarios()
login = Login(registro)
usuario_actual = None
registroINV = RegistroInvitados()
logiINV = LoginInvitado(registroINV)
while True:
    print("Bienvenido")
    print("1. Registro")
    print("2. Inicio de sesión")
    print("3. Salir")
    opcion = input("Ingrese una opción (el numero): ")
    match opcion:
        # Agregar validaciones
        case "1":
            print("1. Registrar como usuario")
            print("2. Registrar como invitado")
            opcion = input("Ingrese una opción (el numero): ")
            match opcion:
                case "1":
                    nombre = input("Ingrese su nombre: ")
                    while validar_nombre(nombre) == False:
                        print("Nombre no válido.")
                        nombre = input("Ingrese su nombre: ")
                    dni = input("Ingrese su DNI: ")
                    d = None
                    while validar_dni(dni) == False or registro.buscar_usuario(d,dni) == False:
                        print("DNI no válido.")
                        dni = input("Ingrese su DNI: ")
                    em = None
                    email = (input("Ingrese su email: "))
                    while  validar_email(email) == False or registro.buscar_usuario(email,em) == False:
                        print("Email no válido.")
                        email = input("Ingrese su email: ")
                    email=email.lower()
                    # Agregue el getpass, simplemente por estetica, busque en internet alguna forma de ocultar la contraseña y me aparecio esto.
                    password = getpass("Ingrese su contraseña (Debe tener al menos 8 caracteres entre esos al menos una letra o numero): ")
                    password_verificacion = getpass("Ingrese su contraseña nuevamente: ")
                    while not validar_password(password) or password != password_verificacion:
                        print("Contraseña no válida.")
                        password = getpass("Ingrese su contraseña: ")
                        password_verificacion = getpass("Ingrese su contraseña nuevamente: ")
                    codigoadmin=input("Ingrese el codigo de administrador: ")
                    usuario = Usuario(nombre, dni,email, password)
                    registro.registrar_usuario(usuario)
                    if validar_email(email) == 'sistema.com.ar' and codigoadmin == '1234':
                        print('Bienvenido administrador')
                        pass
                    else:    
                        print("Usuario registrado correctamente.")
                case "2":
                    nombre = input("Ingrese su nombre: ")
                    while validar_nombre(nombre) == False:
                        print("Nombre no válido.")
                        nombre = input("Ingrese su nombre: ")
                    dni = input("Ingrese su DNI: ")
                    d = None
                    while validar_dni(dni) == False or registroINV.buscar_usuario(d,dni) == False:
                        print("DNI no válido.")
                        dni = input("Ingrese su DNI: ")
                    em = None
                    email = (input("Ingrese su email: "))
                    while  validar_email(email) == False or registroINV.buscar_usuario(email,em) == False:
                        print("Email no válido.")
                        email = input("Ingrese su email: ")
                    email=email.lower()
                    ingresos = 0
                    usuario = Invitado(nombre, dni,email,ingresos)
                    registroINV.registrar_usuario(usuario)
        case "2":
            print("1. Inicio de sesión como usuario")
            print("2. Inicio de sesión como invitado")
            opcion = input("Ingrese una opción (el numero): ")
            match opcion:
                case "1":
                    email = input("Ingrese su email: ")
                    email=email.lower()
                    p = input("Desea ver la contraseña que ingresaste? (s)")
                    match p:
                        case "s":
                            password = input("Ingrese su contraseña: ")
                        case _:
                            password = getpass("Ingrese su contraseña: ")
                    codigoadmin = input("Ingrese el codigo de administrador: ")
                    
                    es_admin=False
                    n = True
                    while n == True:
                        if login.iniciar_sesion(email, password):
                            if validar_email(email)=='sistema.com.ar':
                                while codigoadmin != '1234':
                                    print("Codigo de administrador no válido.")
                                    codigoadmin = input("Ingrese el codigo de administrador: ")
                                es_admin=True
                                usuario_actual = login.usuario_actual
                                n = False
                                
                            else:
                                usuario_actual = login.usuario_actual
                                n = False
                        else:
                            print("Email o contraseña incorrectos.")
                            salir = input("¿Desea salir del programa? (s/n): ")
                            salir = salir.lower()
                            if salir == "s":
                                exit()
                                
                            else:
                                email = input("Ingrese su email: ")
                                email=email.lower()
                                p = input("Desea ver la contraseña que ingresaste? (s)")
                                match p:
                                    case "s":
                                        password = input("Ingrese su contraseña: ")
                                    case _:
                                        password = getpass("Ingrese su contraseña: ")
                                n = True
                    es_invitado = False
                case "2":
                    email = input("Ingrese su email: ")
                    email=email.lower()
                    dni = input("Ingrese su DNI: ")
                    n = True
                    while n == True:
                        if logiINV.iniciar_sesion(email, dni):
                            usuario_actual = logiINV.usuario_actual
                            es_invitado = True
                            es_admin = False
                            n = False
                        else:
                            print("Email o contraseña incorrectos.")
                            salir = input("¿Desea salir del programa? (s/n): ")
                            salir = salir.lower()
                            if salir == "s":
                                exit()
                                
                            else:
                                email = input("Ingrese su email: ")
                                email=email.lower()
                                dni = input("Ingrese su DNI: ")
                                n = True


            print(f'Bienvenido {usuario_actual.nombre}')      
            s = True
            while s == True:
                if usuario_actual is not None:
                    if es_admin:
                        print('1. Agregar vehiculo')
                        print('2. Eliminar vehiculo')
                        print('3. Modificar vehiculo')
                        print('4. ver stcok')
                        print('5. ver ventas')
                        print('6. cerrar sesion')
                        opcion = input("Ingrese una opción (el numero): ")
                        match opcion:
                            # Funciona
                            case "1":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                i = numero_id()
                                n=True
                                while n==True:
                                    agregar_vehiculo_tipo(n, lista_entrelazada, str(i))

                                    if input("¿Desea agregar otro vehículo? (s/n): ") == "s":
                                        i = int(i) + 1
                                        n=True
                                    else:
                                        n=False
                                guardar_stock(nombre_archivo, lista_entrelazada)
                            # funciona
                            case "2":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                print(lista_entrelazada)
                                id = input("Ingrese el id del vehiculo a eliminar: ")
                                actual = lista_entrelazada.cabeza 
                                while actual is not None:
                                    if actual.vehiculo.id == id:
                                        lista_entrelazada.eliminar(id)
                                        print(f"El vehiculo {actual.vehiculo.marca} {actual.vehiculo.modelo} con ID: {actual.vehiculo.id} fue eliminado.")
                                        guardar_stock(nombre_archivo, lista_entrelazada)
                                        break
                                    actual = actual.siguiente
                            # Funciona
                            case "3":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                modificar_dato_vehiculo(lista_entrelazada)
                                guardar_stock(nombre_archivo, lista_entrelazada)
                            # Funciona
                            case "4":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                print(lista_entrelazada)
                            # Ver como implementar bien mathplotlib
                            case "5":
                                nombre_archivo = "ventas.txt"
                                descargar_lista_ventas_estadisticas(nombre_archivo)
                            case "6":
                                lista_invitados=[]
                                b=[]
                                dni=[]
                                listas_email=[]
                                with open ("invitado.txt","r") as archivo:

                                    for linea in archivo:
                                        linea=linea.rstrip()
                                        lista=linea.split(",")
                                        listas_email.append(lista[2])
                                        b.append(int(lista[3]))
                                        lista_invitados.append(lista)
                                    vector=np.array(b)
                                    ordenado=np.sort(vector)
                                    lista_ingresos=vector.tolist()
                                    cont_ord=0
                                    mas_acceso=[]
                                    while cont_ord<5:
                                        maximos=max(vector)
                                        mas_acceso.append(maximos)
                                        cont_ord+=1
                                    for j in range(len(mas_acceso)):
                                        for i in range(len(lista_invitados)):
                                        
                                            if lista_invitados[i][3]==mas_acceso[j]:
                                                dni.append(lista_invitados[i][1])

                                    plt.title(label="DNI por invitados",fontsize=20)
                                    plt.xlabel("DNI")
                                    plt.ylabel("INGRESOS")

                                    plt.bar(dni,mas_acceso)
                                    plt.show()
                                    archivo.close()
                            # si esto no funciona estamo mal
                            case "7":
                                print("Gracias por usar el sistema.")
                                s = False
                            case _:
                                print("Opción inválida.")
                    else:
                        # descargar un archivo de texto con los datos del usuario
                        if es_invitado:
                            lista = []
                            
                            with open("invitado.txt", "r") as archivo:
                                lineas = archivo.readlines()
                                for linea in lineas:
                                    campos = linea.strip().split(",")
                                    lista.append(campos)
                            archivo.close()
                            for i in range(len(lista)):
                                if lista[i][1] == usuario_actual.dni and lista [i][2] == usuario_actual.email:
                                    lista [i][3] = int(lista [i][3]) + 1
                                    break
                            
                            with open("invitado.txt", "w") as archivo:
                                for i in range(len(lista)):
                                    archivo.write(f"{lista[i][0]},{lista[i][1]},{lista[i][2]},{lista[i][3]}\n")
                            archivo.close()
                                
                        
                        print('1. Ver stock')
                        print('2. Comprar vehiculo')
                        print('3. Ver mis compras')
                        print('4. Modificar mis datos')
                        print('5. Cerrar sesion')
                        opcion = input("Ingrese una opción (el numero): ")
                        match opcion:
                            # Funciona
                            case "1":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock_cliente(nombre_archivo)
                                print(lista_entrelazada)
                            # funciona?
                            case "2":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = descargar_stock(nombre_archivo)
                                comprar_vehiculo(buscar_vehiculo(lista_entrelazada), lista_entrelazada, usuario_actual)
                            # si, puede mejorar
                            case "3":
                                nombre_archivo = "ventas.txt"
                                lista = descargar_lista_ventas(nombre_archivo, usuario_actual)
                            # casiquesi
                            case "4":
                                lista_entrelazada = []
                                if es_invitado == False:
                                    try:
                                        with open("usuarios.txt", "r") as archivo:
                                            lineas = archivo.readlines()
                                            for linea in lineas:
                                                campos = linea.strip().split(",")
                                                lista_entrelazada.append(campos)
                                        archivo.close()
                                    except FileNotFoundError:
                                        print("No se encontró el archivo.")
                                else:
                                    try:
                                        with open("invitado.txt", "r") as archivo:
                                            lineas = archivo.readlines()
                                            for linea in lineas:
                                                campos = linea.strip().split(",")
                                                lista_entrelazada.append(campos)
                                        archivo.close()
                                    except FileNotFoundError:
                                        print("No se encontró el archivo.")
                                print("1. Modificar nombre")
                                print("2. Modificar email")
                                if es_invitado == False:
                                    print("3. Modificar contraseña")


                                opcion = input("Ingrese una opción (el numero): ")
                                if es_invitado == False:
                                    match opcion:
                                        case "1":
                                            nombre = input("Ingrese su nombre: ")
                                            while validar_nombre(nombre) == False:
                                                print("Nombre no válido.")
                                                nombre = input("Ingrese su nombre: ")

                                            for i in range(len(lista_entrelazada)):
                                                if lista_entrelazada[i][2] == usuario_actual.email:
                                                    lista_entrelazada[i][0] = nombre
                                        
                                        case "3":
                                            if es_invitado == False:
                                                password = getpass("Ingrese su contraseña: ")
                                                password_verificacion = getpass("Ingrese su contraseña nuevamente: ")
                                                while not validar_password(password) or password != password_verificacion:
                                                    print("Contraseña no válida.")
                                                    password = getpass("Ingrese su contraseña: ")
                                                    password_verificacion = getpass("Ingrese su contraseña nuevamente: ")
                                                for i in range(len(lista_entrelazada)):
                                                    if lista_entrelazada[i][2] == usuario_actual.email:
                                                        lista_entrelazada[i][3] = password
                                        case "2":
                                            em = None
                                            email = (input("Ingrese su email: "))
                                            while  validar_email(email) == False or registro.buscar_usuario(email,em) == False:
                                                print("Email no válido.")
                                                email = input("Ingrese su email: ")
                                            email=email.lower()
                                            for i in range(len(lista_entrelazada)):
                                                    if lista_entrelazada[i][2] == usuario_actual.email:
                                                        lista_entrelazada[i][2] = email
                                        
                                        case _:
                                            print("Opción inválida.")
                                else:
                                    match opcion:
                                        case "1":
                                            nombre = input("Ingrese su nombre: ")
                                            while validar_nombre(nombre) == False:
                                                print("Nombre no válido.")
                                                nombre = input("Ingrese su nombre: ")

                                            for i in range(len(lista_entrelazada)):
                                                if lista_entrelazada[i][2] == usuario_actual.email:
                                                    lista_entrelazada[i][0] = nombre
                                        case "2":
                                            em = None
                                            email = (input("Ingrese su email: "))
                                            while  validar_email(email) == False or registroINV.buscar_usuario(email,em) == False:
                                                print("Email no válido.")
                                                email = input("Ingrese su email: ")
                                            email=email.lower()
                                            for i in range(len(lista_entrelazada)):
                                                    if lista_entrelazada[i][2] == usuario_actual.email:
                                                        lista_entrelazada[i][2] = email
                                        case _:
                                            print("Opción inválida.")

                                if es_invitado == False:
                                    with open("usuarios.txt", "w") as archivo:
                                        for i in range(len(lista_entrelazada)): 
                                            archivo.write(f"{lista_entrelazada[i][0]},{lista_entrelazada[i][1]},{lista_entrelazada[i][2]},{lista_entrelazada[i][3]}\n")
                                    archivo.close()
                                elif es_invitado == True:
                                    with open("invitado.txt", "w") as archivo:
                                        for i in range(len(lista_entrelazada)): 
                                            archivo.write(f"{lista_entrelazada[i][0]},{lista_entrelazada[i][1]},{lista_entrelazada[i][2]},{lista_entrelazada[i][3]}\n")
                                    archivo.close()



                            
                            case "5":
                                print("Gracias por usar el sistema.")
                                s = False
                            case _:
                                print("Opción inválida.")
                                                        
        case "3":
            print("Gracias por usar el sistema.")
            exit()
        case _:
            print("Opción inválida.")



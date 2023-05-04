from Clases import *
from datetime import *
from random import *
from matplotlib import pyplot as plt
import numpy as np
# validaciones
def lista_a_lista_listaentrelazada(lista, Nodo):
    if not lista:
        return None
    head = Nodo(lista[0])
    current = head
    for i in range(1, len(lista)):
        current.next = Nodo(lista[i])
        current = current.next
    return head

def validar_dni(dni):
    if 8 < len(dni)  or  len(dni )< 7 :
        return False
    if not dni.isdigit():
        return False
    return True

def validar_email(email):
    partes = email.split('@')
    if len(partes) != 2:
        return False
    usuario = partes[0]
    dominio = partes[1]
    if not usuario or not dominio:
        return False
    if '.' not in dominio:
        return False
    if usuario[-1] == '.':
        return False
    if '..' in usuario or '..' in dominio:
        return False
    if dominio == 'sistema.com.ar':
        return dominio
    return True

def validar_password(password):
    if len(password) < 8:
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.isalpha() for c in password):
        return False
    return True

def validar_nombre(nombre):
    if  any(c.isdigit() for c in nombre):
        return False
    partes = nombre.split(" ")
    if len(partes) < 2:
        return False
    return True
    

def descargar_stock(nombre_archivo):
    lista_entrelazada = ListaEnlazada()
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            vehiculo=None
            for linea in lineas:
                campos = linea.strip().split(",")
                if campos[0] == "utilitario":
                    vehiculo = Utilitario(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                elif campos[0] == "deportivo":
                    vehiculo = Deportivo(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                elif campos[0] == "electrico":
                    vehiculo = Electrico(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                elif campos[0] == "van":
                    vehiculo = Van(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                elif campos[0] == "compacto":
                    vehiculo = Compacto(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))

                lista_entrelazada.agregar(vehiculo)
        archivo.close()

    except FileNotFoundError:
        print("El archivo no existe")
    return lista_entrelazada

def guardar_stock(nombre_archivo, lista_entrelazada):
    with open(nombre_archivo, "w") as archivo:
        if lista_entrelazada.cabeza is not None:
            actual = lista_entrelazada.cabeza
            tipo= None
            datos=None
            while actual is not None:
                if isinstance(actual.vehiculo, Utilitario):
                    tipo = "utilitario"
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.carga_maxima},{actual.vehiculo.id}\n"
                elif isinstance(actual.vehiculo, Deportivo):
                    tipo = "deportivo"
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.velocidad_maxima},{actual.vehiculo.id}\n"
                elif isinstance(actual.vehiculo, Electrico):
                    tipo = "electrico"
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.tiempo_carga},{actual.vehiculo.id}\n"
                elif isinstance(actual.vehiculo, Van):
                    tipo = "van"
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso}, {actual.vehiculo.asientos},{actual.vehiculo.id}\n"
                elif isinstance(actual.vehiculo, Compacto):
                    tipo = "compacto"
                    datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.tamaño_baul},{actual.vehiculo.id}\n"
                archivo.write(f"{tipo},{datos}")
                actual = actual.siguiente
    archivo.close()
    print(f"Stock guardado en el archivo {nombre_archivo}")
def numero_id():
    try:
        i = descargar_stock("stock.txt")
        i = i.ultimo_nodo().vehiculo.id
        i = i.split("_")[1]
        i=int(i) + 1
        i = str(i)
    except AttributeError:
        i = 0
        i = str(i)
    return i

def agregar_vehiculo_tipo(n, lista_entrelazada,i):
    l = True
    while l:
        tipo= input("Ingrese el tipo de vehículo que desea agregar: ")
        tipo=tipo.lower()
        match tipo:
            case "utilitario":
                marca = input("Ingrese la marca del vehículo: ")
                modelo = input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                nuevo_auto = Utilitario(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: ").lower(),int(input("Ingrese la carga máxima del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case "deportivo":
                marca = input("Ingrese la marca del vehículo: ")
                modelo = input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].lower()+ "_" + i
                nuevo_auto = Deportivo(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: ").lower(), int(input("Ingrese la velocidad máxima del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case "electrico":
                marca = input("Ingrese la marca del vehículo: ")
                modelo = input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                nuevo_auto = Electrico(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese el tiempo de carga del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case "van":
                marca = input("Ingrese la marca del vehículo: ")
                modelo = input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                nuevo_auto = Van(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese la cantidad de asientos del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case "compacto":
                marca = input("Ingrese la marca del vehículo: ")
                modelo = input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                nuevo_auto = Compacto(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese el tamaño del baul del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case _:
                print("Tipo de vehículo no válido")

def eliminar_vehiculo(lista_entrelazada):
    lista=lista_entrelazada.list()
    print(lista)
    n=False
    while n==False:
        marca=input("Ingrese la marca del vehículo que desea eliminar: ")
        modelo=input("Ingrese el modelo del vehículo que desea eliminar: ")
        for i in lista:
            if i.marca==marca and i.modelo==modelo:
                lista_entrelazada.eliminar(i)
                print(f"Se eliminó el vehículo {str(i)} del stock")
                n=True
            else:
                print("Vehículo no encontrado")
                n=True
def modificar_dato_vehiculo(lista_entrelazada):
    lista=lista_entrelazada.list()
    print("Stock de vehículos:")
    print(lista_entrelazada)
    n=False
    while n==False:
        id = input("Ingrese el id del vehículo que desea modificar: ")
        for i in lista:
            if i.id == id:
                print(f"Vehículo encontrado: {str(i)}")
                n=True
                m=False
                while m==False:
                    dato=input("Ingrese el dato que desea modificar: ")
                    dato=dato.lower()
                    match dato:
                        case "marca":
                            i.marca=input("Ingrese la nueva marca: ")
                            m=True
                        case "modelo":
                            i.modelo=input("Ingrese el nuevo modelo: ")
                            m=True
                        case "precio":
                            i.precio=int(input("Ingrese el nuevo precio: "))
                            m=True
                        case "autonomia":
                            i.autonomia=int(input("Ingrese la nueva autonomía: "))
                            m=True
                        case "uso":
                            i.uso=input("Ingrese el nuevo uso: ")
                            m=True
                        case "carga":
                            i.carga=int(input("Ingrese la nueva carga: "))
                            m=True
                        case "velocidad":
                            i.velocidad=int(input("Ingrese la nueva velocidad: "))
                            m=True
                        case "asientos":
                            i.asientos=int(input("Ingrese la nueva cantidad de asientos: "))
                            m=True
                        case "tamaño":
                            i.tamaño=int(input("Ingrese el nuevo tamaño: "))
                            m=True
                        case _:
                            print("Dato no válido")
                            m=True
                    print(f"Se modificó el vehículo {str(i)}")
            else:
                n=True
        return lista
def buscar_vehiculo(lista_vehiculos, marca=None, modelo=None, precio=None, autonomia=None, uso=None):
    lista_vehiculos = lista_vehiculos.list()
    n = False
    while n==False:
        print("Filtros disponibles:\n marca\n modelo\n precio\n autonomia\n uso\n nota: si no desea utilizar un filtro, ingrese 'no'")
        filtro=input("Ingrese el filtro que desea utilizar: ")
        
        filtro=filtro.lower()
        match filtro:
            case "marca":
                marca=input("Ingrese la marca que desea buscar: ")
                marca = marca.lower()
            case "modelo":
                modelo=input("Ingrese el modelo que desea buscar: ")
                modelo = modelo.lower()
            case "uso":
                uso=input("Ingrese el uso que desea buscar: ")
                uso = uso.lower()
            case "precio":
                precio=int(input("Ingrese el precio que desea buscar: "))
            case "autonomia":
                autonomia=int(input("Ingrese la autonomía que desea buscar: "))
            case "no":
                n=True
            case _:
                print("Filtro no válido")               
        m=(input("Desea agregar otro filtro? (s/n): "))
        m=m.lower()
        if m=="s":
            n=False
        else: 
            n=True
    lista_v_filtrado = []
    for vehiculo in lista_vehiculos:
            if marca is not None and vehiculo.marca != marca:
                continue   
            if modelo is not None and vehiculo.modelo != modelo:
                continue
            if precio is not None and int(vehiculo.precio) > precio:
                continue  
            if autonomia is not None and int(vehiculo.autonomia) < autonomia:
                continue
            if uso is not None and vehiculo.uso != uso:
                continue
            lista_v_filtrado.append(vehiculo)
    print("Vehículos encontrados:")
    for vehiculo in lista_v_filtrado:
        print(vehiculo)
    return (lista_v_filtrado)

def comprar_vehiculo(vehiculos_filtrados, lista, usuario):
    n=False
    archivo=open("ventas.txt", "a")
    fecha_hora = datetime.now().date()
    while n==False:
        marca_vehiculo=input("Ingrese la marca del vehículo que desea comprar: ")
        modelo_vehiculo=input("Ingrese el modelo del vehículo que desea comprar: ")
        vehiculo_comprado = None
        for i in vehiculos_filtrados:
            if i.marca==marca_vehiculo and i.modelo==modelo_vehiculo:
                print("Detalle de la compra:")
                print(f"Vehículo: {marca_vehiculo} {modelo_vehiculo}")
                print(f"Precio: ${i.precio}")
                print(f"Transferir ${i.precio} a la siguiente cuenta:")
                print("Nombre del banco: HSBC")
                print("CBU: 0873776281914709007725")
                print("CUIT: 30-12345678-2")
                print("Razon social: ITBA CAR S.R.L")
                print("Mail: ventas@itbacar.org.ar")
                print("Cuenta: CC U$S 105-435261/0 ")
                print(f"Fecha y hora de la compra: {fecha_hora}")
                m = False
                b = True
                while m == False:
                    confirmacion = input("¿Confirma que ha realizado la transferencia? (s/n) ")
                    confirmacion = confirmacion.lower()
                    if confirmacion == "s":
                        print("Compra realizada con éxito")
                        m = True
                        continue
                    elif confirmacion == "n":
                        print("Compra cancelada")
                        m = True
                        b = False
                        n = True
                    else:
                        print("Opción no válida")
                # nuevo
                while b == True:
                    print(f"Se compró el vehículo {marca_vehiculo} {modelo_vehiculo}")
                    actual = lista.cabeza 
                    while actual is not None:
                        if str(actual.vehiculo.marca) == marca_vehiculo and str(actual.vehiculo.modelo) == modelo_vehiculo:
                            vehiculo_comprado = actual.vehiculo
                            id = vehiculo_comprado.id
                            lista.eliminar(id)
                            dato = f"{usuario.dni},{fecha_hora},{vehiculo_comprado.marca},{vehiculo_comprado.modelo},{vehiculo_comprado.precio}\n"
                            archivo.write(f'{dato}')
                            break
                        actual = actual.siguiente
                    guardar_stock("stock.txt",lista)
                    n=True
                    b=False
            else:
                n=True
    archivo.close()
    return vehiculos_filtrados

def descargar_lista_ventas(nombre_archivo, usuario_actual):
    lista_entrelazada = ListaEnlazada()
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            compra = None
            contador = 0
            total = 0
            contadormarca = 0
            tupla_marca = ()
            tupla_contador = ()
            for linea in lineas:
                campos = linea.strip().split(",")
                if campos[0] == usuario_actual.email:
                    compra = (f"Mail: {campos[0]}, Fecha: {campos[1]}, Marca: {campos[2]}, Modelo: {campos[3]}, Precio: ${campos[4]}")
                    contador += 1
                    total += int(campos[4])
                    lista_entrelazada.agregar(compra)   
            archivo.close()
            
            l = True
            while l == True:
                print("Estadisticas Disponibles:")
                print(f"1. Total Compras por Marca \n2. Cantidad de Compras Realizadas \n3. Total Gastado \n4. Detalle de Compras Realizadas \n5. Volver al menú principal")
                opcion = input("Ingrese el número de la estadística que desea ver: ")
                match opcion:    
                    case "1":
                        print("Total de compras por marca")
                        lista_entrelazada1 = lista_entrelazada.list()
                        for i in range(len(lista_entrelazada1)):
                            marca = lista_entrelazada1[i]
                            marca = marca.split(", ")[2]
                            marca = marca.split("Marca: ")[1]
                            contadormarca = 0
                            for x in range(len(lista_entrelazada1)):
                                marca2 = lista_entrelazada1 [x]
                                marca2 = marca2.split(", ")[2]
                                marca2 = marca2.split("Marca: ")[1]
                                if marca2 == marca:
                                    contadormarca += 1
                                        
                            if marca not in tupla_marca: 
                                tupla_marca += tuple(marca.split())
                                tupla_contador += tuple(str(contadormarca).split())
                            if marca in tupla_marca:
                                pass
                                    
                        
                                
                        labels = tupla_marca
                        sizes = convertir_tupla_en_lista(tupla_contador)

                        fig1, ax1 = plt.subplots()
                        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                        shadow=True, startangle=90)
                        ax1.axis('equal')

                        plt.show()
                        inp = input("Desea ver otra estadistica(s/n): ")
                        if inp == "s":
                            l = True
                        else:
                            l = False
                    case "2":
                        print(f"Usted ha realizado {contador} compra/s")
                        inp = input("Desea ver otra estadistica(s/n): ")
                        if inp == "s":
                            l = True
                        else:
                            l = False
                    case "3":
                        print(f"El total gastado es de ${total}")
                        inp = input("Desea ver otra estadistica(s/n): ")
                        if inp == "s":
                            l = True
                        else:
                            l = False
                    case "4":
                        print("------------------------------Detalle de compras realizadas------------------------------")
                        print(lista_entrelazada)
                        inp = input("Desea ver otra estadistica(s/n): ")
                        if inp == "s":
                            l = True
                        else:
                            l = False
                    case "5":
                        l = False
                    case _:
                        print("Opción no válida")
                        l = True
    except FileNotFoundError:
        print("No ha realizado ninguna compra")
    
def modificar_datos(lista, usuario):
    registro=RegistroUsuarios()
    n=False
    while n==False:
        dato=input("Ingrese el dato que desea modificar: ")
        dato=dato.lower()
        match dato:
            case "nombre":
                usuario.nombre=input("Ingrese el nuevo nombre: ")
                n=True
            case "email":
                usuario.email=input("Ingrese el nuevo email: ")
                n=True
            case "contraseña":
                usuario.contraseña=input("Ingrese la nueva contraseña: ")
                n=True
            case _:
                print("Dato no válido")
                n=True
    registro.cargar_usuarios(usuario)

def saque_todos_int(string):
    id = ""
    for i in string:
        try:
            int(i)
            id += i
        except:
            if i == "_":
                id = id[::-1]
                return id 
            pass

def descargar_stock_cliente(nombre_archivo):
    lista_entrelazada = ListaEnlazada()
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            vehiculo=None
            for linea in lineas:
                campos = linea.strip().split(",")
                if campos[0] == "utilitario":
                    vehiculo = Utilitario(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                elif campos[0] == "deportivo":
                    vehiculo = Deportivo(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                elif campos[0] == "elictrico":
                    vehiculo = Electrico(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                elif campos[0] == "van":
                    vehiculo = Van(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                elif campos[0] == "compacto":
                    vehiculo = Compacto(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                lista_entrelazada.agregar(vehiculo)
                
        archivo.close()

    except FileNotFoundError:
        print("El archivo no existe")
    return lista_entrelazada

def convertir_tupla_en_lista(tupla):
    lista = []
    for elemento in tupla:
        lista.append(elemento)
    return lista


def descargar_lista_ventas_estadisticas(nombre_archivo):
    lista_entrelazada = ListaEnlazada()
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            compra = None
            recaudacion = 0
            contador = 0
            contadormarca = 0
            tupla_marca = ()
            tupla_contador = ()
            tupla_precio = ()
            tupla_fecha = ()
            
            for linea in lineas:
                campos = linea.strip().split(",")
                compra = (f"Mail: {campos[0]}, Fecha: {campos[1]}, Marca: {campos[2]}, Modelo: {campos[3]}, Precio: ${campos[4]}")
                lista_entrelazada.agregar(compra)
                recaudacion += int(campos[4])
                contador += 1
                

        archivo.close() 
        l = True
        while l == True:
            print("opciones: ")
            print("1. Cantidad de ventas por marca")
            print("2. Recaudacion total por dia")
            print("3. Recaudacion total")
            print("4. Cantidad de autos vendidos")
            print("5. Detalle de todas las ventas")
            print("6. Salir")
            op = input("Ingrese la opcion que desea(numero): ")
            match op:
                case "1":

                    lista_entrelazada1 = lista_entrelazada.list()
                    for i in range(len(lista_entrelazada1)):
                        marca = lista_entrelazada1[i]
                        marca = marca.split(", ")[2]
                        marca = marca.split("Marca: ")[1]
                        contadormarca = 0
                        for x in range(len(lista_entrelazada1)):
                            marca2 = lista_entrelazada1 [x]
                            marca2 = marca2.split(", ")[2]
                            marca2 = marca2.split("Marca: ")[1]
                            if marca2 == marca:
                                contadormarca += 1
                            
                        if marca not in tupla_marca: 
                            tupla_marca += tuple(marca.split())
                            tupla_contador += tuple(str(contadormarca).split())
                        if marca in tupla_marca:
                            pass
                        
            
                    
                    labels = tupla_marca
                    sizes = convertir_tupla_en_lista(tupla_contador)

                    fig1, ax1 = plt.subplots()
                    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
                    ax1.axis('equal')

                    plt.show()

                    inp = input("Desea ver otra estadistica(s/n): ")
                    if inp == "s":
                        l = True
                    else:
                        l = False
                case "2":
                    lista_entrelazada2 = lista_entrelazada.list()
                    for i in range(len(lista_entrelazada2)):
                        fecha = lista_entrelazada2 [i]
                        fecha = fecha.split(", ")[1]
                        fecha = fecha.split("Fecha: ")[1]
                        contadorfac = 0
                        for x in range(len(lista_entrelazada2)):
                            fecha2 = lista_entrelazada2 [x]
                            fecha2 = fecha2.split(", ")[1]
                            fecha2 = fecha2.split("Fecha: ")[1]
                            if fecha2 == fecha:
                                precio = lista_entrelazada2 [x]
                                precio = precio.split(", ")[4]
                                precio = precio.split("Precio: ")[1]
                                precio = precio.split("$")[1]
                                contadorfac += int(precio)
                        if fecha not in tupla_fecha: 
                            tupla_fecha += tuple(fecha.split())
                            tupla_precio += tuple(str(contadorfac).split())
                        if fecha in tupla_fecha:
                            pass
                    
                    fig, ax = plt.subplots()
                    x = tupla_fecha
                    counts = convertir_tupla_en_lista(tupla_precio)
                    for i in range(len(counts)):
                        counts[i] = int(counts[i])
                    ax.bar(x, counts)
                    ax.set_ylabel('Recaudación')
                    ax.set_title('Recaudación Total por Día')          
                    plt.show()
                    inp = input("Desea ver otra estadistica(s/n): ")
                    if inp == "s":
                        l = True
                    else:
                        l = False
                case "3":
                        print(f"La facturación total es de: ${recaudacion}")
                        inp = input("Desea ver otra estadistica(s/n): ")
                        if inp == "s":
                            l = True
                        else:
                            l = False
                case "4":
                    print(f"Se han realizado {contador} venta/s")
                    inp = input("Desea ver otra estadistica(s/n): ")
                    if inp == "s":
                        l = True
                    else:
                        l = False
                case "5":
                    print("Detalle de las ventas:")
                    lista_entrelazada4 = lista_entrelazada.list()
                    for i in range(len(lista_entrelazada4)):
                        print(lista_entrelazada4[i])
                    inp = input("Desea ver otra estadistica(s/n): ")
                    if inp == "s":
                        l = True
                    else:
                        l = False
                case "6":
                    l = False
                case _:
                    print("Dato no válido")
                    l = True
    except FileNotFoundError:
        print("No ha realizado ninguna compra")

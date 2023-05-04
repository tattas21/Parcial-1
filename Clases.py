#Clases Usuarios
# clase usuario general de esta se hereda administrador y cliente
class Usuario:
    def __init__(self, nombre, dni,email, password):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.password = password


    def __str__(self):
        return f"{self.nombre} {self.dni} {self.email}"


class administrador(Usuario):
    def __init__(self,nombre,dni,email,password, es_admin):
        super().__init__(nombre,dni,email,password)
        self.es_admin = None
    def es_administrador(self):
        if self.email == 'sistema.com.ar':
            self.es_admin = True
            return self.es_admin 
        else:
            self.es_admin = False
            return self.es_admin 
    


class RegistroUsuarios:
    def __init__(self):
        self.usuarios = []
        self.archivo = "usuarios.txt"
        self.cargar_usuarios()

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        self.guardar_usuarios()

    def guardar_usuarios(self):
        with open(self.archivo, "w") as f:
            for usuario in self.usuarios:
                f.write(f"{usuario.nombre},{usuario.dni},{usuario.email},{usuario.password}\n")
        f.close()

    def cargar_usuarios(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    nombre, dni, email, password = linea.strip().split(",")
                    self.usuarios.append(Usuario(nombre,dni,email,password))
            f.close()
        except FileNotFoundError:
            pass
    def buscar_usuario(self, email, dni):
        for usuario in self.usuarios:
            if usuario.email == email or usuario.dni == dni:
                print(f"El usuario ya existe")
                return False
        return None
# Ver opcion sin clase
class Login:
    def __init__(self, registro_usuarios):
        self.registro_usuarios = registro_usuarios
        self.usuario_actual = None

    def iniciar_sesion(self, email, password):
        for usuario in self.registro_usuarios.usuarios:
            if usuario.email == email and usuario.password == password:
                self.usuario_actual = usuario
                return True
        return False

    def cerrar_sesion(self):
        self.usuario_actual = None

class Vehiculo:
    def __init__(self, modelo, marca, precio,  autonomia, uso, id):
        self.modelo = modelo
        self.marca = marca
        self.precio = precio
        self.autonomia = autonomia
        self.uso = uso
        self.id = id
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: {self.precio},Autonomia: {self.autonomia}, Uso: {self.uso}"

class Utilitario(Vehiculo):
    def __init__(self, marca, modelo, precio, autonomia, uso, carga_maxima, id):
        super().__init__(modelo, marca, precio,autonomia, uso, id)
        self.carga_maxima = carga_maxima
    def __str__(self):
        return super().__str__() + f", Carga máxima: {self.carga_maxima}, ID: {self.id}"
        
class Deportivo(Vehiculo):
    def __init__(self, marca, modelo, precio, autonomia, uso, velocidad_maxima, id):
        super().__init__(modelo, marca, precio,autonomia, uso, id)
        self.velocidad_maxima = velocidad_maxima
    def __str__(self):
        return super().__str__() + f", Velocidad máxima: {self.velocidad_maxima}, ID: {self.id}"
        
class Electrico(Vehiculo):
    def __init__(self, marca, modelo, precio,autonomia, uso, tiempo_carga, id):
        super().__init__(modelo, marca, precio,autonomia, uso,  id)
        self.tiempo_carga = tiempo_carga
    def __str__(self):
        return super().__str__() + f", Tiempo de carga: {self.tiempo_carga}, ID: {self.id}"
        
class Van(Vehiculo):
    def __init__(self, marca, modelo, precio,autonomia, uso, asientos, id):
        super().__init__(modelo, marca, precio, autonomia, uso, id)
        self.asientos = asientos

    def __str__(self):
        return super().__str__() + f", Asientos: {self.asientos}, ID: {self.id}"
        
class Compacto(Vehiculo):
    def __init__(self, marca, modelo, precio, autonomia, uso,tamaño_baul, id):
        super().__init__(modelo, marca, precio,autonomia, uso, id)
        self.tamaño_baul = tamaño_baul
    def __str__(self):
        return super().__str__() + f", Tamaño del baul: {self.tamaño_baul}, ID: {self.id}"
    

class Nodo:
    def __init__(self, vehiculo, siguiente = None):
        self.vehiculo = vehiculo
        self.siguiente = siguiente

        

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, vehiculo):
        nuevo_nodo = Nodo(vehiculo)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            return
    
    def eliminar(self, id):
        
        if self.cabeza is None:
            return
        elif self.cabeza.vehiculo.id == id:
            self.cabeza = self.cabeza.siguiente   
        else:
            actual = self.cabeza
            while actual is not None:
                if actual.siguiente.vehiculo.id == id:
                    if actual.siguiente.siguiente == None:
                        actual.siguiente = None
                        return self
                    else:
                        actual.siguiente = actual.siguiente.siguiente
                    return self
                actual = actual.siguiente
    
    def __str__(self):
        if self.cabeza is None:
            return "La lista está vacía"
        else:
            actual = self.cabeza
            resultado = str(actual.vehiculo)
            while actual.siguiente is not None:
                actual = actual.siguiente
                resultado += f"\n{str(actual.vehiculo)}"
            return resultado
    def list(self):
        lista = []
        nodo = self.cabeza
        while nodo is not None:
            lista.append(nodo.vehiculo)
            nodo = nodo.siguiente
        return lista
    def ultimo_nodo(self):
        while self.cabeza.siguiente is not None:
            self.cabeza = self.cabeza.siguiente
        return self.cabeza


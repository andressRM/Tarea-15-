class NodoInventario:
    def __init__(self, producto, cantidad):
        # inicializamos el nodo con el nombre del producto y su cantidad
        self.producto = producto
        self.cantidad = cantidad
        self.siguiente = None

class ListaEnlazadaInventario:
    def __init__(self):
        # inicializamos la cabeza de la lista
        self.cabeza = None

    def agregar_producto(self, producto, cantidad):
        # creamos un nuevo nodo
        nuevo_nodo = NodoInventario(producto, cantidad)
        # si la lista esta vacia el nuevo nodo es la cabeza
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            # recorremos hasta el final y agregamos el nodo
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print(f"\nexito producto {producto} agregado al inventario")

    def deshacer_ultimo(self):
        # elimina el ultimo producto agregado
        if self.cabeza is None:
            return
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return
        actual = self.cabeza
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = None

    def mostrar_inventario(self):
        # imprimimos todos los productos
        if self.cabeza is None:
            print("el inventario esta vacio")
            return
        actual = self.cabeza
        while actual is not None:
            print(f"producto {actual.producto} cantidad {actual.cantidad}")
            actual = actual.siguiente

class ColaPedidos:
    def __init__(self):
        # inicializamos la cola
        self.cola = []

    def agregar_pedido(self, cliente):
        # agregamos el pedido al final
        self.cola.append(cliente)
        print(f"\nexito pedido de {cliente} ingresado al sistema")

    def procesar_pedido(self):
        # sacamos el primer pedido
        if len(self.cola) == 0:
            print("\nno hay pedidos pendientes")
            return None
        cliente = self.cola.pop(0)
        print(f"\ndespachando el pedido de {cliente}")
        return cliente

    def deshacer_ultimo(self):
        # elimina el ultimo pedido
        if len(self.cola) > 0:
            self.cola.pop()

    def mostrar_pedidos(self):
        # mostramos los pedidos
        if len(self.cola) == 0:
            print("no hay pedidos en espera")
            return
        print("lista de pedidos en espera")
        for cliente in self.cola:
            print(f"cliente {cliente}")

class PilaHistorial:
    def __init__(self):
        # inicializamos la pila
        self.pila = []

    def registrar_accion(self, tipo_accion):
        # guardamos la accion en la cima
        self.pila.append(tipo_accion)

    def deshacer_accion(self):
        # sacamos la ultima accion
        if len(self.pila) == 0:
            print("\nno hay acciones recientes para deshacer")
            return None
            
        ultima_accion = self.pila.pop()
        return ultima_accion

# menu rincipal
if __name__ == "__main__":
    inventario = ListaEnlazadaInventario()
    pedidos = ColaPedidos()
    historial = PilaHistorial()

    print("bienvenido al sistema de gestion integrado")

    while True:
        print("\nmenu principal de opciones")
        print("1 registrar producto en inventario")
        print("2 registrar un nuevo pedido")
        print("3 despachar el primer pedido")
        print("4 deshacer la ultima accion")
        print("5 mostrar todo el sistema")
        print("6 salir del programa")
        
        opcion = input("\ningrese el numero de la opcion deseada: ")

        if opcion == "6":
            print("\ncerrando el sistema hasta pronto")
            break
            
        elif opcion == "1":
            prod = input("\ningrese el nombre del producto: ")
            try:
                cant = int(input("ingrese la cantidad en numeros: "))
                inventario.agregar_producto(prod, cant)
                historial.registrar_accion("inventario")
            except ValueError:
                print("\nerror debe ingresar un numero valido")
                
        elif opcion == "2":
            cliente = input("\ningrese el nombre del cliente: ")
            pedidos.agregar_pedido(cliente)
            historial.registrar_accion("pedido")
            
        elif opcion == "3":
            pedidos.procesar_pedido()
            
        elif opcion == "4":
            accion = historial.deshacer_accion()
            if accion == "inventario":
                inventario.deshacer_ultimo()
                print("\nse borro el ultimo registro del inventario")
            elif accion == "pedido":
                pedidos.deshacer_ultimo()
                print("\nse borro el ultimo pedido ingresado")
                
        elif opcion == "5":
            print("\nreporte actual del sistema")
            print("inventario disponible")
            inventario.mostrar_inventario()
            print("-------------------")
            pedidos.mostrar_pedidos()
            
        else:
            print("\nopcion no valida por favor ingrese un numero del uno al seis")
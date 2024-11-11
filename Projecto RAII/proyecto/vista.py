
class AeroChinquihueVista:
    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def mostrar_resumen_ventas(self, resumen):
        print(resumen)

    def mostrar_vuelos_en_servicio(self, vuelos):
        print("\n----- Vuelos en servicio -----")
        print(vuelos)

    def obtener_datos_reserva(self):
        destino = input("Ingrese el destino: ")
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        hora = input("Ingrese la hora (HH:MM): ")
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        tipo_avion = input("Ingrese el tipo de avión: ")
        return destino, fecha, hora, nombre_cliente, tipo_avion

    def obtener_datos_encomienda(self):
        destino = input("Ingrese el destino para la encomienda: ")
        peso = float(input("Ingrese el peso de la encomienda (kg): "))
        fecha = input("Ingrese la fecha de envío (YYYY-MM-DD): ")
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        tipo_avion = input("Ingrese el tipo de avión: ")
        return destino, peso, fecha, nombre_cliente, tipo_avion

    def obtener_datos_vuelo(self):
        destino = input("Ingrese el destino del vuelo: ")
        fecha = input("Ingrese la fecha del vuelo (YYYY-MM-DD): ")
        hora = input("Ingrese la hora del vuelo (HH:MM): ")
        tipo_avion = input("Ingrese el tipo de avión: ")
        capacidad = int(input("Ingrese la capacidad del avión: "))
        peso_total = float(input("Ingrese el peso total del vuelo (kg): "))
        return destino, fecha, hora, tipo_avion, capacidad, peso_total

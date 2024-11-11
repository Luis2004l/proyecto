
class AeroChinquihueControlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def reservar_pasaje(self):
        destino, fecha, hora, nombre_cliente, tipo_avion = self.vista.obtener_datos_reserva()
        mensaje = self.modelo.reservar_pasaje(destino, fecha, hora, nombre_cliente, tipo_avion)
        self.vista.mostrar_mensaje(mensaje)

    def enviar_encomienda(self):
        destino, peso, fecha, nombre_cliente, tipo_avion = self.vista.obtener_datos_encomienda()
        mensaje = self.modelo.enviar_encomienda(destino, peso, fecha, nombre_cliente, tipo_avion)
        self.vista.mostrar_mensaje(mensaje)

    def agregar_vuelo(self):
        destino, fecha, hora, tipo_avion, capacidad, peso_total = self.vista.obtener_datos_vuelo()
        mensaje = self.modelo.agregar_vuelo(destino, fecha, hora, tipo_avion, capacidad, peso_total)
        self.vista.mostrar_mensaje(mensaje)

    def ver_resumen_ventas(self):
        resumen = self.modelo.resumen_ventas()
        self.vista.mostrar_resumen_ventas(resumen)

    def ver_vuelos_en_servicio(self):
        vuelos = self.modelo.vuelos_en_servicio()
        self.vista.mostrar_vuelos_en_servicio(vuelos)

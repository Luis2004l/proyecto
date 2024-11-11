class AeroChinquihueModelo:
    def __init__(self):
    
        self.precios_pasajes = {
            "Cochamó": 20000, "Puelo Bajo": 20000, "Contao": 20000, "Rio Negro": 25000,
            "Pupelde": 25000, "Chepu": 30000, "Ayacara": 30000, "Pillán": 40000,
            "Reñihue": 40000, "Isla Quenac": 40000, "Palqui": 40000, "Chaitén": 50000, "Santa Bárbara": 50000
        }

       
        self.precios_encomiendas = {
            "Cochamó": 5000, "Puelo Bajo": 5000, "Contao": 5000, "Rio Negro": 6000,
            "Pupelde": 6000, "Chepu": 8000, "Ayacara": 8000, "Pillán": 12000,
            "Reñihue": 12000, "Isla Quenac": 12000, "Palqui": 12000, "Chaitén": 15000, "Santa Bárbara": 15000
        }

        
        self.aviones = {
            "CESSNA 310": {"capacidad": 5, "peso_maximo": 910},
            "CESSNA 208 CARAVAN": {"capacidad": 9, "peso_maximo": 1315},
            "LET 410 UVP-E20": {"capacidad": 19, "peso_maximo": 1800}
        }

       
        self.ventas = []

        
        self.vuelos = [
            {"destino": "Cochamó", "fecha": "2024-11-15", "hora": "10:00", "avion": "CESSNA 310", "capacidad": 4, "peso_total": 700},
            {"destino": "Puelo Bajo", "fecha": "2024-11-16", "hora": "14:00", "avion": "CESSNA 208 CARAVAN", "capacidad": 8, "peso_total": 1200},
            {"destino": "Contao", "fecha": "2024-11-17", "hora": "16:00", "avion": "LET 410 UVP-E20", "capacidad": 18, "peso_total": 1500},
            {"destino": "Chaitén", "fecha": "2024-11-18", "hora": "08:00", "avion": "CESSNA 208 CARAVAN", "capacidad": 7, "peso_total": 1300}
        ]

    def reservar_pasaje(self, destino, fecha, hora, nombre_cliente, tipo_avion):
        if destino in self.precios_pasajes:
            precio_pasaje = self.precios_pasajes[destino]
            if self.verificar_disponibilidad_vuelo(destino, fecha, hora, tipo_avion):
                self.ventas.append({
                    "tipo": "pasaje", "destino": destino, "fecha": fecha, "hora": hora,
                    "cliente": nombre_cliente, "precio": precio_pasaje, "avion": tipo_avion
                })
                return f"Reserva de pasaje confirmada para {nombre_cliente} a {destino} el {fecha} a las {hora}. Precio: ${precio_pasaje}."
            else:
                return f"No hay vuelos disponibles a {destino} el {fecha} a las {hora}."
        else:
            return f"Destino inválido: {destino}."

    def enviar_encomienda(self, destino, peso, fecha, nombre_cliente, tipo_avion):
        if destino in self.precios_encomiendas:
            precio_encomienda = self.precios_encomiendas[destino] * peso
            if self.verificar_disponibilidad_vuelo(destino, fecha, "cualquier hora", tipo_avion):
                self.ventas.append({
                    "tipo": "encomienda", "destino": destino, "fecha": fecha, "peso": peso,
                    "cliente": nombre_cliente, "precio": precio_encomienda, "avion": tipo_avion
                })
                return f"Encomienda registrada para {nombre_cliente} a {destino} el {fecha}. Precio: ${precio_encomienda}."
            else:
                return f"No hay vuelos disponibles a {destino} el {fecha}."
        else:
            return f"Destino inválido: {destino}."

    def verificar_disponibilidad_vuelo(self, destino, fecha, hora, tipo_avion):
        if tipo_avion in self.aviones:
            capacidad_avion = self.aviones[tipo_avion]["capacidad"]
            peso_maximo_avion = self.aviones[tipo_avion]["peso_maximo"]
            for vuelo in self.vuelos:
                if vuelo["destino"] == destino and vuelo["fecha"] == fecha and vuelo["hora"] == hora and vuelo["avion"] == tipo_avion:
                    if vuelo["capacidad"] < capacidad_avion and vuelo["peso_total"] < peso_maximo_avion:
                        return True
        return False

    def agregar_vuelo(self, destino, fecha, hora, tipo_avion, capacidad, peso_total):
        if tipo_avion in self.aviones:
            self.vuelos.append({
                "destino": destino, "fecha": fecha, "hora": hora, "avion": tipo_avion,
                "capacidad": capacidad, "peso_total": peso_total
            })
            return f"Vuelo agregado a {destino} el {fecha} a las {hora} con {tipo_avion}."
        else:
            return f"Tipo de avión inválido: {tipo_avion}."

    def resumen_ventas(self):
        ventas_pasajes = [venta for venta in self.ventas if venta["tipo"] == "pasaje"]
        ventas_encomiendas = [venta for venta in self.ventas if venta["tipo"] == "encomienda"]
        total_ventas = sum(venta["precio"] for venta in self.ventas)
        return (f"Total de ventas de pasajes: {len(ventas_pasajes)}\n"
                f"Total de ventas de encomiendas: {len(ventas_encomiendas)}\n"
                f"Total de ingresos: ${total_ventas}")

    def vuelos_en_servicio(self):
        vuelos_info = []
        for vuelo in self.vuelos:
            vuelos_info.append(f"- Destino: {vuelo['destino']}, Fecha: {vuelo['fecha']}, Hora: {vuelo['hora']}, Avión: {vuelo['avion']}")
        return "\n".join(vuelos_info)

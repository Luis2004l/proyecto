#integrantes: Luis Allendes

from proyecto.modelo import AeroChinquihueModelo
from proyecto.vista import AeroChinquihueVista
from proyecto.controlador import AeroChinquihueControlador

def main():
    modelo = AeroChinquihueModelo()
    vista = AeroChinquihueVista()
    controlador = AeroChinquihueControlador(modelo, vista)

    while True:
        print("\n----- Menú -----")
        print("1. Reservar pasaje")
        print("2. Enviar encomienda")
        print("3. Agregar vuelo")
        print("4. Ver resumen de ventas")
        print("5. Ver vuelos en servicio")
        print("6. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            controlador.reservar_pasaje()
        elif opcion == "2":
            controlador.enviar_encomienda()
        elif opcion == "3":
            controlador.agregar_vuelo()
        elif opcion == "4":
            controlador.ver_resumen_ventas()
        elif opcion == "5":
            controlador.ver_vuelos_en_servicio()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()

menu = {
    "1" : "COP a USD",
    "2" : "USD a EUR",
    "3" : "EUR a COP",
    "4" : "Salir"
}

def mostrar_menu(menu):
    print("\n📌 Conversor de moneda")
    for key, nombre in menu.items():
        print(f"{key}, {nombre}")

    opcion = input("\nElije uan opcion (1-4): ")
    return opcion

def convertir(moneda_origen, moneda_destino, tasa):
    cantidad = input(f"\nIngresa la cantidad en {moneda_origen}: ")

    try:
        cantidad_float = float(cantidad)
    except ValueError:
        print("❌ Debes ingresar un número válido")
        return

    resultado = cantidad_float * tasa
    print(f"💱 {cantidad_float:.2f} {moneda_origen} equivalen a {resultado:.2f} {moneda_destino}")

def confirmar_salida():
    respuesta = input("¿Seguro quieres salir? (s/n): ").strip().lower()
    return respuesta == "s"

def main():

    while True:

        opcion = mostrar_menu(menu)

        if opcion == "1":
            convertir("COP", "USD", 1 / 4000)
        elif opcion == "2":
            convertir("USD", "EUR", 0.88)
        elif opcion == "3":
            convertir("EUR", "COP", 4900)
        else:
            if opcion == "4":
                if confirmar_salida():
                    print("\nHasta luego 👋🏽")
                    break
                continue

        if opcion not in menu:
            print("\n❌ Opcion Invalida, Intentalo de nuevo")
            continue

if __name__ == "__main__":
    main()
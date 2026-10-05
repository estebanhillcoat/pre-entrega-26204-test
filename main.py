import colorama
from colorama import Fore, Back, Style, init

# Inicializar colorama con autoreset
init(autoreset=True)

productos = []

while True:
    opciones = input(
        "Elija la opción deseada\n"
        "R - Remover\n"
        "S - Salir\n"
        "B - Buscar\n"
        "A - Agregar\n"
        "L - Listar productos\n"
    ).strip().upper()

    match opciones:
        case "R":
            producto_remover = input("\nIngrese producto a quitar: \n").strip()
            if producto_remover in productos:
                productos.remove(producto_remover)
                print(Fore.GREEN + f"\n{producto_remover} quitado con éxito.\n")
            else:
                print(Fore.RED + f"\n{producto_remover} no está en la lista.\n")

        case "S":
            print(Fore.YELLOW + "\nSaliendo del programa...")
            break

        case "A":
            producto_agregar = input("\nIngrese producto a agregar: \n").strip()
            if producto_agregar:
                productos.append(producto_agregar)
                print(Fore.GREEN + f"\n{producto_agregar} agregado con éxito.\n")
            else:
                print(Fore.RED + "\nEl nombre no puede estar vacío.\n")

        case "L":
            if productos:
                print(Fore.CYAN + "\nListado de productos:")
                for i, producto in enumerate(productos, start=1):
                    print(f"{i}. {producto}")
            else:
                print(Fore.YELLOW + "\nNo hay productos registrados.\n")

        case "B":
            producto_a_buscar = input("\nIngrese producto a buscar: \n").strip()
            if producto_a_buscar in productos:
                print(Fore.GREEN + f"\n{producto_a_buscar} está en stock.\n")
            else:
                print(Fore.RED + f"\n{producto_a_buscar} no está en stock.\n")

        case _:
            print(Fore.RED + "\nOpción inválida, intente nuevamente.\n")

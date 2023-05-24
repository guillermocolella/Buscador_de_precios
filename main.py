from ws import *


def main():
    print("  ========================================")
    print(" | - BIENVENIDOS AL BUSCADOR DE PRECIOS - |")
    print("  ========================================\n")
    opcion = input("Introduce el producto que quieres buscar >> ")
    print("")

    print("************************************************************")
    print(f"      >>>>>>  Buscando {opcion.upper()} en Jumbo  <<<<<<<<<")
    print("************************************************************\n")
    productos_jumbo = scrap_products_jumbo(opcion)
    print("------------------------------------------------------------")
    print(
        f" >>>>>>  Mostrando precios de {opcion.upper()} en Jumbo  <<<<<<<<<")
    print("------------------------------------------------------------\n")
    for producto in productos_jumbo:
        print(f'{producto["Productos de Jumbo"]} = {producto["Precio"]}')
        print("\n")

    print("************************************************************")
    print(f"      >>>>>>  Buscando {opcion.upper()} en ChangoMas  <<<<<<<<<")
    print("************************************************************\n")
    productos_chango = scrap_products_chango(opcion)
    print("------------------------------------------------------------------")
    print(
        f" >>>>>>  Mostrando precios de {opcion.upper()} en ChangoMas  <<<<<<<<<")
    print("------------------------------------------------------------------\n")
    for producto in productos_chango:
        print(f'{producto["Productos de Changomas"]} = {producto["Precio"]}')
        print("\n")

    print("************************************************************")
    print(f"    >>>>>>  Buscando {opcion.upper()} en Coto  <<<<<<<<<")
    print("************************************************************\n")
    productos_coto = scrap_products_coto(opcion)
    print("--------------------------------------------------------------")
    print(f" >>>>>>  Mostrando precios de {opcion.upper()} en Coto  <<<<<<<<<")
    print("--------------------------------------------------------------\n")
    for producto in productos_coto:
        print(f'{producto["Productos de Coto"]} = {producto["Precio"]}')
        print("\n")

    print("************************************************************")
    print(f"      >>>>>>  Buscando {opcion.upper()} en DIA  <<<<<<<<<")
    print("************************************************************\n")
    productos_dia = scrap_products_dia(opcion)
    print("------------------------------------------------------------------")
    print(f" >>>>>>  Mostrando precios de {opcion.upper()} en DIA  <<<<<<<<<")
    print("------------------------------------------------------------------\n")
    for producto in productos_dia:
        print(f'{producto["Productos de Dia"]} = {producto["Precio"]}')
        print("\n")

    print(" ---------------------------------------------------------")
    print("| - SE GUARDO LA INFORMACION EN EL ARCHIVO Precios.xlsx - |")
    print(" ---------------------------------------------------------\n")

    # Se pregunta al usuario si quiere visualizar el archivo generado
    respuesta = input("¿Queres abrir el archivo Excel? (S/N) : ").upper()
    print("")
    if respuesta == "S":
        os.startfile(cwd)
    else:
        print("El archivo se guardo en el Escritorio\n")

if __name__ == '__main__':

    main()

while True:
    nuevo = input("¿Buscar otro Producto? (S/N) : ").upper()
    print("")
    if nuevo == "S":
        main()
    else:
        print("Cerrando el programa...")
        browser.quit()
        break

# This is a sample Python script.
import Functions as fc
import miguel as mg


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_Tu_vecino():
    fc.printLinea()
    print("  Bienvenido a Tu Vecino ")
    fc.printLinea()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_Tu_vecino()
    fc.ingresoCodigo()
    fc.printLinea()
    cantidad = float(input("ingrese la cantidad del producto por unidad "))
    fc.printLinea()
    valorUnitario = float(input("Ingrese el valor unitario del producto "))
    fc.printLinea()
    fc.subTotal(cantidad, valorUnitario)
    fc.printLinea()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

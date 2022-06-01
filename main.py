#import modules
import Functions as fc
#function example
def print_Tu_vecino():
    fc.printLinea()
    print("  Bienvenido a Tu Vecino ")
    fc.printLinea()

#Run main
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

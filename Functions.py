def print_Tu_vecino():
    printLinea()
    print("  Bienvenido a Tu Vecino ")
    printLinea()


# Function input code and name product
def datos():
    cantidades=1;
    cantidadProductos = int(input("Ingrese el numero de productos: "))
    while cantidades <= cantidadProductos:
        _codigo_ = input("Ingrese el codigo del producto: ")
        _nombre_product = input("Ingrese el nombre del producto: ")
        cantidad = float(input("Ingrese la cantidad del producto: "+_nombre_product))
        _valorUnitario = float(input("Ingrese el valor unitario del producto: "))
        ingresarDetalleProducto(_codigo_, _nombre_product, cantidad, _valorUnitario)
        subTotal(cantidad, _valorUnitario)
        cantidades+=1
    print("Muchas gracias por su compra")


def ingresarDetalleProducto(_codigo_, _nombreProduct,_cantidad,_valorUnitario):
    printLinea()
    print("Codigo producto: ", _codigo_, "\nDetalle Producto: ", _nombreProduct,"\t Cantidad: ",_cantidad,"\t Valor Unitario: ",_valorUnitario)




# Function estimate subtotal of buy
def subTotal(_cantidad_: float, _valorUnitario_: float):
    if (_cantidad_ and _valorUnitario_ <= 0):
        print("No se puede realizar la operacion")
    else:
        _sub_total = float(_valorUnitario_ * _cantidad_)
        totalConIva(_sub_total)


# Function of total buy with total iva
def totalConIva(total: float):
    print("Escoga la tipo de iva\n Opcion 1: Excento de iva\n opcion 2:Bienes Iva 5%\nOpcion 3: General Iva 19%")
    opcion=int(input("Ingrese el tipo de iva"))
    if(opcion==1):
        print("Subtotal: ",total,"\t Total: ",total,"\t Excento de iva")
    elif(opcion==2):
        iva=0.5
        totalIva=(total*iva)+total
        print("Subtotal: ", total, "\t Total: ", totalIva, "\t Iva 5%")
    elif(opcion==3):
        iva=0.19
        totalIva=(total*iva)+total
        print("Subtotal: ", total, "\t Total: ", totalIva, "\t Iva 19%")
# print = how invoice
def printLinea():
    print("=" * 50)

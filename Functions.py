def ingresoCodigo():
    _codigo_ = input("Ingrese el codigo del producto")
    _nombre_product = input("Ingrese el nombre del producto")
    printLinea()
    print("El producto ", _nombre_product, "Tiene el codigo ", _codigo_)


def subTotal(_cantidad_:float, _valorUnitario_:float):
    if (_cantidad_ and _valorUnitario_ <= 0):
        print("No se puede realizar la operacion")
    else:
        _sub_total = float(_valorUnitario_ * _cantidad_)
        print("Cantidad ", _cantidad_)
        printLinea()
        print("Valor Unitario ", _valorUnitario_)
        printLinea()
        print("Subtotal ", _sub_total)
        totalConIva(_sub_total)




def totalConIva(total:float):
    _valor_iva_ = float(0.19)
    _siTiene = input("Tiene iva? si o no ")
    if (_siTiene == 'si'):
        _total_iva_ =(_valor_iva_ * total)  + total
        printLinea()
        print("Total Compra ", _total_iva_, " IVA", _valor_iva_ * 100, " %")
        if (_total_iva_ > 100000):
            descuentoHoy = 0.20
            totalDescuento =   _total_iva_ - (_total_iva_ * descuentoHoy)
            printLinea()
            print("Tiene descuento del ", descuentoHoy * 100, "%")
            printLinea()
            print("Total con descuento ", totalDescuento)
    elif (_siTiene == "no"):
        printLinea()
        print("Total compra ", total, " No tiene IVA")

def printLinea():
    print("="*50)
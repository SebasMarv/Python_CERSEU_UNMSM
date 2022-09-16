def descuento(vmonto):
    xdcto=0
    if(vmonto>1000):
        xdcto=(vmonto * 0.2)
    else:
        xdcto= 0
    return xdcto

def montopago(vmonto,vdcto):
    xpago=(vmonto-vdcto)
    return xpago
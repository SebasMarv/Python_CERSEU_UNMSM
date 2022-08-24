"""
5. La aerolínea Global por campaña realiza vuelos nacionales, internacional América e Europa –
Asia aun precio general para cualquier destino. Para cada vuelo la forma de calcular la venta de
pasaje es diferente. Se debe también ingresar nombre de clientes y cantidad de pasajes:
Vuelo Nacional: s/350 x pasaje, 3% de seguro de vuelo, 18% de IGV
Vuelo Internacional América: s/1500 x pasaje, impuesto de salida 4.5%, 3.5% de seguro de
vuelo, 18% de IGV
Vuelo Internacional Europa-Asia: s/2500 x pasaje, impuesto de salida 6.5%, 5.5% de seguro de
vuelo, 18% de IGV
"""

def problema5(tipo,cantidad):
    if tipo=='Nacional':
        pasaje=350*cantidad
        seguro=pasaje*0.03
        impuesto = 0
    elif tipo=='America':
        pasaje=1500*cantidad
        seguro=pasaje*0.035
        impuesto=pasaje*0.045
    else:
        pasaje=2500*cantidad
        impuesto=pasaje*0.60
        seguro=pasaje*0.055
    igv = pasaje*0.18
    neto=pasaje+impuesto+seguro+igv
    print('Monto pasaje: S/',round(pasaje,1))
    print('Monto seguro: S/',round(seguro,1))
    print('Impuesto de salida: S/',round(impuesto,1))
    print('IGV: S/',round(igv,1))
    print('Precio neto: S/',round(neto,1))
    print('-------------------------------------')

problema5('Nacional',3)
problema5('America',3)
problema5('Europa',3)
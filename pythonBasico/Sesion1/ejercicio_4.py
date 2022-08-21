"""
Débora, Raquel y Sófia aportan cantidades de dinero para formar un capital.
Diseñe un programa que determine el capital formado y el porcentaje de dicho
capital que aporta cada uno.
"""

def problema4(debora,raquel,sofia):
    capital = debora + raquel + sofia
    porc_debora = 100*debora/capital
    porc_raquel = 100*raquel/capital
    porc_sofia = 100*sofia/capital
    print('- - - - - - - - - - - - - - - - -')
    print('Capital es S/',capital)
    print('Porcentaje de Debora: ',round(porc_debora,1),'%')
    print('Porcentaje de Raquel: ',round(porc_raquel,1),'%')
    print('Porcentaje de Sofia: ',round(porc_sofia,1),'%')
    print('- - - - - - - - - - - - - - - - -')

#round(variable, {numero de decimales}) sirve para redondear :)

problema4(4500,1500,3600)
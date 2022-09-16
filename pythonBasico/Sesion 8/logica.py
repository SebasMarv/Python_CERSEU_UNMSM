def pago(horas,pago_hora):
  if horas>48:
    pago_inicial=48*pago_hora
    extra=((horas-48)*pago_hora)*2
    total_dia=pago_inicial+extra
  else:
    total_dia=pago_hora*horas

def pago_semanal(total):
  total_semanal=total*7
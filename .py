import time
time_duration=5
print("Nuevo cliente")
print("Buenas tardes")
edad=str(input("Edad:"))
clima=str(input("Temperatura del día:"))
if (edad=="menor" and clima=="frio"):
    print("La sugerencia es una bebida: fría")
if (edad=="menor" and clima=="templado"):
    print("La sugerencia es una bebida: fría")
if (edad=="menor" and clima=="calido"):
    print("La sugerencia es una bebida: fría")
if (edad=="adulto" and clima=="frio"):
    print("La sugerencia es una bebida: caliente")
if (edad=="adulto" and clima=="templado"):
    print("La sugerencia es una bebida: fria")
if (edad=="adulto" and clima=="calido"):
    print("La sugerencia es una bebida: fria")
if(edad=="mayor" and clima=="frio"):
    print("La sugerencia es una bebida: caliente")
if(edad=="mayor" and clima=="templado"):
    print("La sugerencia es una bebida: caliente")
if(edad=="mayor" and clima=="calido"):
    print("La sugerencia es una bebida: caliente")
time.sleep(time_duration)

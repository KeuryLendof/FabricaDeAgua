import datetime
fecha= datetime.datetime.now()
import os

print("Agua Lendof💦")

galon_agua = 65
hielo = 25

def menu():
    print("""
1) Galon de Agua🌊_ _ _ _ _ _ 65
2) Hielo❄️_ _ _ _ _ _ _ _ _ _ 25""")
menu()

def compra():
    while True:
        cantidad = int(input("Cuantos galones de agua desea comprar: "))
        opc = (cantidad*galon_agua)

        cantidad1 = int(input("Cuantas fundas de hielo desea comprar: "))
        opc1 = (cantidad1*hielo)

        suma_total = (opc+opc1)
        print("FACTURA")
        print(fecha.strftime('%d/%m/%Y'))
        print("EL TOTAL DE SU COMPRA ES : {}".format(suma_total))

        cont = int(input("Desea continuar con la factura 1) Si | 2) No : "))
        if cont == 1:
            print("Imprimiendo............")
            break
        
        if cont == 2:
            os.system('cls')
            print("⬆⬆Factura Cancelada⬆⬆")
            print("⬇⬇⬇Factura Nueva⬇⬇⬇")       
compra()
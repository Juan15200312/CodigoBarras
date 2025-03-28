from barcode import EAN13
from barcode.writer import ImageWriter

def ingresarDatos():
    salir=True
    while salir:
        try:
            numero=int(input("Ingresa un numero: "))
            if len(str(numero))==12:
                directorio= input("Ingresa donde desea guardar el archivo: ")
                salir=False
                return numero, directorio
            else:
                print("El numero tiene que contener 12 digitos !")
        except ValueError:
            print("El numero ingresado no es valido")

def generarCoBarras(numero, directorio):
    try:
        nombre = "codigo_barras"
        codigo_barras = EAN13(str(numero), writer=ImageWriter())
        codigo_barras.save(fr"{directorio}/{nombre}")
        print("Codigo barras generado exitosamente")
    except Exception as e:
        print("Ops, ocurrio un error: ", e)

def main():
    numero, directorio = ingresarDatos()
    generarCoBarras(numero, directorio)

if __name__ == '__main__':
    main()
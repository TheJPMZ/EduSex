import qrcode

#Funciones para generar el codigo qr y mandar la informacion necesaria al empleado

def generarCodigoQR(metodo, codigo, codigo_compra):
    #Genera el codigo QR con la informacion del pedido
    img= qrcode.make(f'método:{metodo}| codigo_usuario:{codigo} | codigo_compra:{codigo_compra}')
    img.save('Compra.png')
    
generarCodigoQR('Efectivo', '123456789', '123456789')
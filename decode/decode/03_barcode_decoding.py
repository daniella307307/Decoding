import pyzxing

reader = pyzxing.BarCodeReader()
barcode = reader.decode('C:/Users/user/Documents/Decoding-codes/decode/decode/barcode.jpg')

if barcode:
    print("Decoded Data:", barcode[0]['raw'])
else:
    print("No barcode found.")
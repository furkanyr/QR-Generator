import pyqrcode

url = input("enter url to generate QR code: ")

qr_code = pyqrcode.create(url)
qr_code.svg("C:/Users/Yerinde/Desktop/out_QR", 8)
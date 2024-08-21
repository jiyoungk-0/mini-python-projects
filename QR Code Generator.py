import qrcode

data = 'Don\'t forget to subscribe'

# Generate QR code image
img = qrcode.make(data)

# Define file path to save QR code image
img.save('~/QRcode/qrcode.png')

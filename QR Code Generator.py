import qrcode

# URL to be encoded in the QR code
url = 'https://www.google.com'

# Generate QR code image
img = qrcode.make(url)

# Define file path to save QR code image
img.save('~/QRcode/qrcode.png')

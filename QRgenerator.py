import pyqrcode
from pyqrcode import QRCode

# String which you would like turned into a QRCode
s = input("Enter a URL or string to convert: \n")
file = input("Name the file: \n")

# Generate the code
code = pyqrcode.create(s)

# Save the file as .SVG
code.svg((file + ".svg"), scale=8)
# create a function that collects a text and converts it to QR Code
# Save the QR Code in Image
# run Function
# install library called 'pip install qrcode image'


import qrcode as qr

img = qr.make("Shubham Gurjar")  # this will show in QR code After Scanned
img.save("SG.png") # Your File will be save as this name



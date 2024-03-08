# create a function that collects a text and converts it to QR Code
# Save the QR Code in Image
# run Function
# install library called 'pip install qrcode image'
# install librart called 'pip install PIL'


import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10, border = 4)
qr.add_data("https://github.com/Shubham2303199723")
qr.make(fit = True)
img = qr.make_image(fill_color = "#005B41", back_color = "#0F0F0F")
img.save("GITHUB@Shubham_Gurjar.png")
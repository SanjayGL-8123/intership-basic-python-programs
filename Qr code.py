import qrcode

# pip install qrcode[pil]
# Replace this with your desired link
link =input(" Enter the URL and Sentence : ")

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border
)
qr.add_data(link)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="white", back_color="red")

# Save the image as PNG
img.save("qrcode.png")
print("QR code saved as qrcode.png")
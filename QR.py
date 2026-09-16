import qrcode

# Your Streamlit app URL
url = "https://wirleed.github.io/](https://wirleed.github.io/"

# Create QR code
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save QR code image
# Save QR code image
img.save("walid.png")

print("✅ QR code generated and saved as 'walid.png'")

# Custom Styled QR Code Generator (`Qr code.py`)

Generates a customized, styled Quick Response (QR) code PNG image from any URL or text input.

---

## 📋 Overview

Takes user input (such as a website URL, contact info, or message), configures a QR code with custom matrix size, error correction, and high-contrast styling (white fill on a red background), and exports the output to `qrcode.png`.

---

## 🛠️ Requirements & Dependencies

- **Python Version:** Python 3.x (Tested on Python 3.9.4)
- **Required Libraries:**
  ```powershell
  pip install qrcode pillow
  ```
  *(Status: **Installed** ✅ `qrcode==8.2`, `pillow==11.3.0`)*

---

## 🚀 How to Run

```powershell
python "Qr code.py"
```

> **Note:** Enclose filename with quotation marks due to the space in the name.

---

## 🔍 Code Breakdown

```python
import qrcode

# Input link or text
link = input(" Enter the URL and Sentence : ")

# Configure QR code matrix specifications
qr = qrcode.QRCode(
    version=1,                                    # Matrix size (1 is 21x21)
    error_correction=qrcode.constants.ERROR_CORRECT_L, # ~7% error recovery
    box_size=10,                                  # Pixel dimension of each module box
    border=4,                                     # Thickness of quiet zone border
)
qr.add_data(link)
qr.make(fit=True)

# Generate image with custom color palette
img = qr.make_image(fill_color="white", back_color="red")

# Save file
img.save("qrcode.png")
print("QR code saved as qrcode.png")
```

### Key Concepts:
- `qrcode.QRCode`: Factory object configuring dimensions, margins, and error correction levels.
- `ERROR_CORRECT_L`: Low error correction level recovering up to 7% damaged or obscured data.
- `make_image(fill_color=..., back_color=...)`: Allows customizing QR code styling colors (e.g. white pattern over red background).
- **Output:** Writes the output image to `qrcode.png` in the current folder.

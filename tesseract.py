import pytesseract as tess
from PIL import Image


def pytesseract(filename):
    text = tess.image_to_string(Image.open(filename))

    return text

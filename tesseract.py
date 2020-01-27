import pytesseract as tess
from PIL import Image


def pytesseract(filename, code):

    try:
        text = tess.image_to_string(Image.open(filename))
    except:
        text = ''

    return text

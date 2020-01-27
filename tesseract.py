import pytesseract as tess
from PIL import Image


def pytesseract(filename, code):

    try:
        text = tess.image_to_string(Image.open(filename))
        print("successfully detected:\t" + text)
    except IOError as e:
        text = ''
        print("exception is thrown:\t " + e)

    return text

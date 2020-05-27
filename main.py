import pyscreenshot as ImageGrab
import pytesseract as pt
import time

keyword='batman'
exitMessage='I AM THE NIGHT'

# main loop
while True:
    # take the screenshot
    im = ImageGrab.grab()
    # put it on greyscale (helps ocr sometimes)
    grey = im.convert('LA')

    # OCR converts it to text 
    message = pt.image_to_string(grey)
    
    # check if you have the keyword anywhere in the screen
    if keyword in message:
        exit(exitMessage)
    else:
        time.sleep(1)

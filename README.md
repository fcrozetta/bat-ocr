# bat-ocr
Command line program that reads your screen every second and checks if you have the word batman anywhere. If you have, it exits the program. That is it. seriously.

## Why
I created this for educational purposes. I wanted to try something different, and new to me. this is it.

## How it works
we have the main loop that will take one screenshot of the entire screen, and uses tesseract to read the image. If there is a batman anywhere, it exits with a default message of  "I AM THE NIGHT", otherwise sleeps for one second, before going back to the start of the loop.

## tech used

- pyscreenshot
- pytesseract

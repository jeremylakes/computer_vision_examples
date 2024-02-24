#Text to speech library
from gtts import gTTS
import os
#text recognition
import cv2
import pytesseract

#read test text image
image = cv2.imread('./testing_text.jpg')

#config
config = ('-1 eng --oem 1 --psm 3')

#pytesseract
text = pytesseract.image_to_string(image, config=config)

#print example text
text = text.split('n')
print(text)

myText = 'This is text to speech'
language = 'en'

myObj = gTTS(text=myText, lang=language, slow=False)

#save audio to an mp3 file
filename = "audioFile.mp3"
myObj.save(filename)

#playing converted file
os.system(f"start {filename}")
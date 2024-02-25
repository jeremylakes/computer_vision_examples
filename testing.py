import cv2 as cv2
import pytesseract

#Text to speech library
from gtts import gTTS
import os

#img = cv2.imread('testing_text.jpg')

# Adding custom options
#custom_config = r'--oem 3 --psm 6'
#pytesseract.image_to_string(img, config=custom_config)

#import pytesseract
#import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#set up camera
cam = cv2.VideoCapture(1)

# Load image
img = cv2.imread("unnamed.png")
#resize large image
img = cv2.resize(img, (600, 360))
# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply threshold to convert to binary image
threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# Pass the image through pytesseract

cv2.imshow('testing image', threshold_img)
myText = pytesseract.image_to_string(threshold_img)
# Print the extracted text
print(myText)

#text to speech stuff
#config
config = ('-1 eng --oem 1 --psm 3')

#print example text
myText = myText.split('n')
#print(text)

#myText = 'This is text to speech'
language = 'en'

myObj = gTTS(text=myText, lang=language, slow=False)

#save audio to an mp3 file
filename = "audioFile.mp3"
myObj.save(filename)

#playing converted file
os.system(f"start {filename}")

#img = cv2.resize(img, (600, 360))
#print(pytesseract.image_to_string(img))
#cv2.imshow('Result', img)
cv2.waitKey(0)
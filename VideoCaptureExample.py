# program to capture single image from webcam in python 
#import to check which OS is running this script
from sys import platform

from gtts import gTTS
import os
import pytesseract
# importing OpenCV library 
import cv2 as cv
import time
#from batch_grammar_check import *

if platform == "win32":
    #For Windows (this hasto be here or there iwll be an import error...)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
elif platform == "linux":
#For Linux (this has to be here or there will be an import error...)
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# initialize the camera 
# If you have multiple camera connected with  
# current device, assign a value in cam_port  
# variable according to that 
cam_port = 1
#cam = cv.VideoCapture(cam_port) 

# define a video capture object 
vid = cv.VideoCapture(cam_port) 

while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
  
    # Display the resulting frame 
    cv.imshow('frame', frame) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
#vid.release() 
# Destroy all the windows 
#cv.destroyAllWindows() 
  
# reading the input using the camera 
result, image = vid.read() 
  
# If image will detected without any error,  
# show result 
if result: 

    image = cv.resize(image, (600, 600))
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    threshold_img = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

    # showing result, it take frame name and image  
    # output 
    cv.imshow("frame", threshold_img) 
  
    # saving image in local storage 
    cv.imwrite("read_this_text.png", threshold_img) 

    #pytesseract
    myText = pytesseract.image_to_string(threshold_img)
  
    time.sleep(5)

    #config
    config = ('-1 eng --oem 1 --psm 3') 

    language = 'en'

    myObj = gTTS(text=myText, lang=language, slow=False)

    #print example text
    text = myText.split('n')
    print(myText)

    #save audio to an mp3 file
    filename = "textToSpeech.mp3"
    myObj.save(filename)

    #playing converted file
    os.system(f"start {filename}")

    # If keyboard interrupt occurs, destroy image  
    # window 
    cv.waitKey(0) 
    cv.destroyWindow("frame") 
  
# If captured image is corrupted, moving to else part 
else: 
    print("No image detected. Please! try again") 

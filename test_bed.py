from sys import platform
if platform == "linux" or platform == "linux2":
    # linux
    print('This is a Linux OS')
elif platform == "darwin":
    # OS X
    print('This is a Mac OS')
elif platform == "win32":
    # Windows...
    print('This is a Windows OS')

#from transformers import pipeline

#corrector = pipeline(
#              'text2text-generation',
#              'pszemraj/flan-t5-large-grammar-synthesis',
#              )
#raw_text = 'i can has cheezburger'
#results = corrector(raw_text)
#print(results)

import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # this is the magic!

#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

r, frame = cap.read()
...
print('Resolution: ' + str(frame.shape[0]) + ' x ' + str(frame.shape[1]))
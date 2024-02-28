# computer_vision_examples
Collection of Python files that contain example use cases of computer vision primarily using the Open CV library. 

Need to pip install gTTS pyttsx3 playsound soundfile transformers datasets sentencepiece openai

Install Optimum from Hugging Face for the use of transformers here: https://huggingface.co/docs/optimum/installation

pip install --break-system-packages --upgrade-strategy eager install optimum[onnxruntime]

pip install -U -q --break-system-packages --upgrade-strategy eager install transformers accelerate

Install pytesseract and update your PATH to include the location that it was installed. For Linux it should be here:  
  export PATH="/usr/bin":$PATH
Then (for Linux) you have to include the following line in the file you call it:
  pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
and for Windows you have to include the following line in the file you call it:
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

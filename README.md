# Automatify

### Contributers:
- Kirti ([KDHIR004](https://github.com/KDHIR004))
- Chittesh ([Chittesh1999](https://github.com/Chittesh1999))

#### Video Demo:  https://youtu.be/dQw4w9WgXcQ

#### Description:
Automatify is a web consisting of 3 broad tools developed to ease the workflow in day to day life. The user ends up in main webpage which then leads to different routes for each tool and then sub routes for each feature in the tool. The index page has three tools on top right corner namely Speech Recognition, Translator, Text Extraction and contact. clicking on speech recognition takes you to the index of that tool which then has two options of using a file as an input or a mic input from browser. clicking on Translator takes you to a form from where you can enter the text and choose the language upon submission of which shows the translated text on left pane. clicking on image extraction takes you to a file form where you can upload the image and upon submission yields the extracted image from the image.

### Implemenation :-
The implementaion is fairly simple as Flask is used to build this webapp. We have expanded our knowledge in python, javascript, css and other requisites as we required them while building this web app. We used javascript and python to program the backend of the project and Bootstrap css and javascript to program the front or the user ui of the webapp
The routes-
`/`: is for homepage or index of webapp
`/text_extraction`: is for image extraction tool
`/speech`: is for the index of Speech recognition tool
`/translator`: is for the translator tool
`/wavfile`: is for the speech recognition via file upload .wav file being only supported format
`/mic`: is for the speech recognition via microphone input from the browser


### Setup:-
Libraries used consists of flask for building basic Flask structure.
SpeechRecognition for Speech Recognition tool, googletrans for Language translator and PIL and pytesseract for Image text extraction tool

Install these Libraries required to run the app by
  > `pip install requirements.txt`

Add the path to your tesseract installation in windows for it to work on top of code in app.py
  > `pytesseract.pytesseract.tesseract_cmd = 'C://PATH'`


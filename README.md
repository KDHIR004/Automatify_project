# Automatify

### Contributers:
- Kirti ([KDHIR004](https://github.com/KDHIR004))
- Chittesh ([Chittesh1999](https://github.com/Chittesh1999))

#### Video Demo:  https://youtu.be/dQw4w9WgXcQ

#### Description:
Automatify is a web consisting of 3 broad tools developed to ease the workflow in day to day life. The user ends up in main webpage which then leads to different routes for each tool and then sub routes for each feature in the tool. The index page has three tools on top right corner namely Speech Recognition, Translator, Text Extraction and contact. clicking on speech recognition takes you to the index of that tool which then has two options of using a file as an input or a mic input from browser. clicking on Translator takes you to a form from where you can enter the text and choose the language upon submission of which shows the translated text on left pane. clicking on image extraction takes you to a file form where you can upload the image and upon submission yields the extracted image from the image.

#### Implemenation :-
The implementaion is fairly simple as Flask is used to build this webapp. We have expanded our knowledge in python, javascript, css and other requisites as we required them while building this web app. We used javascript and python to program the backend of the project and Bootstrap css and javascript to program the front or the user ui of the webapp 
The routes:
- `/`: This route is for homepage or index of webapp designed using bootstarp css and other requisites.
- `/text_extraction`: This route is for image extraction tool which uses a file submission form to extract the written text in the image.
- `/speech`: This route is for the index of Speech recognition tool where user gets an option of selecting method of speech recognition by either a file or thorugh input by microphone.
- `/translator`: This route is for the translator tool which takes user to a form which upon submission yields the translated text in the language selected.
- `/wavfile`: This route is for the speech recognition via file upload .wav file being only supported format which also uses a file submission form same as in text extraction tool.
- `/mic`: This route is for the speech recognition via microphone input from the browser which uses java script as we found it difficult to make a recording of user's voice and then send it to the flask backend to process it.


### Setup:-
Libraries used consists of flask for building basic Flask structure.
SpeechRecognition for Speech Recognition tool, googletrans for Language translator and PIL and pytesseract for Image text extraction tool

Install these Libraries required to run the app by
  > `pip install requirements.txt`

Add the path to your tesseract installation in windows for it to work on top of code in app.py
  > `pytesseract.pytesseract.tesseract_cmd = 'C://PATH'`


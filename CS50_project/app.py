from flask import Flask, render_template, request
import speech_recognition as sr
from googletrans import Translator
import pytesseract
from PIL import Image
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///text.db"
#database
db= SQLAlchemy(app)

#create db model
class text(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    txt = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    # create a function  to string  
    def __repr__(self):
        return '<Text %r>' % self.id
@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/text_extraction", methods=['GET','POST'])
def text():
    # initializing the speech text
    text = ""
    if request.method == "POST":
        # sanity check and extraction of text from audio file        
        file = request.files["file"]    
        try:
            image = Image.open(file)
            text = pytesseract.image_to_string(image)
        except:
            return render_template('nofile.html')
    return render_template('textFile.html', text=text)

@app.route("/speech", methods=['GET','POST'])
def speech():
    return render_template('speech.html')

@app.route("/translator", methods=['GET', 'POST'])
def translator():
    if request.method == 'POST':
        try:
            Dest = request.form["select-language"]
            sentence = request.form["text-to-translate"].lower()
            
            translator = Translator()
            translated_text = translator.translate(sentence, dest=Dest)
            text = translated_text.text
        except:
            text = "ERROR :please try again"
        return render_template('translator.html',result=text)
    return render_template('translator.html')
    
@app.route("/wavfile", methods=['GET', 'POST'])
def wavfile():
    # initializing the speech text
    speech = ""
    if request.method == "POST":
        # sanity check and extraction of text from audio file        
        file = request.files["file"]    
        try:
            with sr.AudioFile(file) as source:
                data = sr.Recognizer().record(source)
            speech = sr.Recognizer().recognize_google(data)
        except:
            return render_template('nofile.html')
    return render_template('wav.html', speech=speech)

@app.route("/mic", methods=['GET', 'POST'])
def mic():
    return render_template('mic.html')

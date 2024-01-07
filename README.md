# Automatify

### Contributers:
- Kirti ([KDHIR004](https://github.com/KDHIR004))
- Chittesh ([Chittesh1999](https://github.com/Chittesh1999))


#### Description:
Automatify is a web application consisting of three tools developed to ease day-to-day workflows. Users land on the main webpage, which then leads to different routes for each tool and sub-routes for each feature. The index page has three tools in the top right corner: Speech Recognition, Translator, Text Extraction, and a Contact tool. Clicking on Speech Recognition takes you to the tool's index, where you can choose between using a file or microphone input. Clicking on Translator takes you to a form where you can enter text and choose the desired language. Clicking on Text Extraction takes you to a file form for uploading an image, yielding the extracted text upon submission.


## Implementation:
The implementation of Automatify is a fusion of robust backend development using Flask, sophisticated frontend design with Bootstrap, and the seamless integration of powerful Python libraries. The project showcases a harmonious blend of technologies, demonstrating the team's mastery of Python, JavaScript, and CSS.


### Technologies Used:
#### Backend:
- **Flask:** The core of Automatify, providing a solid foundation for building web applications with Python.
- **Flask-SQLAlchemy:** Empowering the application with a lightweight yet powerful SQLite database to store and manage data efficiently.

#### Frontend:
- **Bootstrap CSS:** Elevating the user interface with responsive and visually appealing design elements.
- **Bootstrap JavaScript:** Enhancing user interactions with dynamic and engaging frontend functionalities.

#### Speech Recognition Tool:
- **SpeechRecognition Library:** Leveraged to seamlessly convert spoken language into text, offering users the flexibility to choose between file upload or microphone input.

#### Translator Tool:
- **Googletrans Library:** Empowering the application with robust language translation capabilities, enabling users to effortlessly translate text in various languages.

#### Text Extraction Tool:
- **PIL (Pillow) and Pytesseract Libraries:** Utilized to extract textual information from images, enhancing the tool's versatility.

### Development Approach:
The team meticulously expanded their expertise in Python, JavaScript, and CSS as they navigated the intricacies of building a web application that seamlessly integrates multiple tools. The frontend development embraced modern design principles, ensuring a user-friendly experience. JavaScript was strategically employed for dynamic functionalities, particularly in the challenging task of implementing speech recognition via microphone input.

### Folder Structure:
The project's folder structure is organized for clarity and maintainability. Key components, including static assets, templates, and backend logic, are thoughtfully organized to facilitate easy navigation for developers.

`
/Automatify
    /static
        /css
        /js
        /img
    /templates
        index.html
        speech.html
        translator.html
        textFile.html
        wav.html
        mic.html
    app.py
    requirements.txt
`


## Setup:
Libraries used:
- Flask for basic structure.
- SpeechRecognition for Speech Recognition.
- googletrans for Language Translator.
- PIL and pytesseract for Image Text Extraction.

Install required libraries by running:
 > `pip install -r requirements.txt`

Add the path to your tesseract installation in windows for it to work on top of code in app.py
  > `pytesseract.pytesseract.tesseract_cmd = 'C://PATH'`

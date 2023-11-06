import os
from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, send_file
from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
import excel as ex

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Convert JPG to Text
def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def getIndex (array,substring):
    for i, string in enumerate(array):
        if substring in string:
            return i
    return -1

def process_data(filename):
    print(f"Processing ", filename)

    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    text_content = extract_text_from_image(image_path)
    lines = text_content.split("\n")
    lines = [line for line in lines if line.strip()]
    for i in range(len(lines)):
        print(i,":",lines[i])

    categories = ["Type of lecture","Lecture Title", "Resource Person Name", "Designation","Company Name","City,Country","Course Code/Course Title","Date","Time","Mode/Venue","Coordinators"]
    spotters = [["Cordially invites you all for",1],
        ["by",-1],
        ["by",1],
        ["by",2],
        ["by",3],
        ["by",4],
        ["Date:",-1],
        ["Date:",0],
        ["Time:",0],
        ["Time:",1],
        ["Faculty Coordinators:",0]]
    
    text_data = [[]]
    for i in range(0,len(categories)):
        # if (i==10):
        #     data = lines[getIndex(lines,spotters[i][0]) + spotters[i][1]]
        #     if (data[-4:]==" and"):
        #         data += " " + lines[getIndex(lines,spotters[i][0]) + spotters[i][1] + 1]
        #     text_data.append([categories[i],data])
        # else:
        #     text_data.append([categories[i],lines[getIndex(lines,spotters[i][0]) + spotters[i][1]]])
        
        if (i==10):
            data = lines[getIndex(lines,spotters[i][0]) + spotters[i][1]]
            if (data[-4:]==" and"):
                data += " " + lines[getIndex(lines,spotters[i][0]) + spotters[i][1] + 1]
            text_data[0].append(data)
        else:
            text_data[0].append(lines[getIndex(lines,spotters[i][0]) + spotters[i][1]])

        # print(text_data[i])
    print(text_data)
    excel_path = ex.saveAsExcel(filename.split('.')[0],text_data)

    print("Processing complete")
    return excel_path


@app.route("/")
def home():
    return render_template("home.html")

@app.route('/handle_flyer', methods=['POST'])
def handle_data():
    if not 'file' in request.files:
       return make_response(jsonify({'msg':'No files uploaded'}), 400)
    file = request.files['file']
    filename = secure_filename(file.filename)
    print(filename)
    file.save(os.path.join(app.root_path,app.config['UPLOAD_FOLDER'],filename))

    excel_path = process_data(filename)
    return send_file(excel_path, as_attachment=True)
    
if __name__ == "__main__":
    app.run(debug=True)

import os
from flask import Flask, render_template, jsonify, request, make_response, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/handle_flyer', methods=['POST'])
def handle_data():
    if not 'file' in request.files:
       return make_response(jsonify({'msg':'No files uploaded'}), 400)
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return make_response(jsonify({'file':filename}), 200)

@app.route('/download_data')
def donwload_data():
    return "Donwload"
    
if __name__ == "__main__":
    app.run(debug=True)

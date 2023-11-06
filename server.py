import os
from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, send_file
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def process_data(filename):
    print(f"Processing ", filename)
    print("Processing complete")

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

    process_data(filename);

    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(path, as_attachment=True)
    
if __name__ == "__main__":
    app.run(debug=True)

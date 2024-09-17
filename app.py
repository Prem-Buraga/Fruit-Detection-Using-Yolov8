
import os
import shutil

from flask import Flask, flash, redirect, render_template, request, url_for
from PIL import Image
from ultralytics import YOLO

app = Flask(__name__)

# Load the YOLO model
model = YOLO("templates/best.pt")

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # Save the uploaded file
            filename = "uploaded_image.jpg"
            file_path = os.path.join(app.root_path, 'uploads', filename)
            file.save(file_path)
            # Perform object detection
            results = model.predict(source=file_path, save=True, project="Detect", name="TF")
            output_image_path = os.path.join("Detect", "TF", filename)
            # Open the image
            saved_image = Image.open(output_image_path)
            saved_image.show()  # Display the image using the default image viewer
            # Delete the Detect folder
            shutil.rmtree("Detect")
            return render_template('result.html', image_file=output_image_path)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)

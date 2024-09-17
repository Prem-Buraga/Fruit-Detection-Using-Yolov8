from PIL import Image
from ultralytics import YOLO
import os
import shutil

# Load the YOLO model
model = YOLO("best.pt")

# Input image path
input_image_path = "0000a16e4b057580_jpg.rf.7e6dce029fb67f01eb19aa730a5d5c2e.jpg"

# Predict on an image and save it with specified project and name
results = model.predict(source=input_image_path, save=True, project="Detect", name="TF")

# Construct the image path
output_image_path = os.path.join("Detect", "TF", os.path.basename(input_image_path))

# Open the image
saved_image = Image.open(output_image_path)
saved_image.show()  # Display the image using the default image viewer

# Delete the Detect folder
shutil.rmtree("Detect")

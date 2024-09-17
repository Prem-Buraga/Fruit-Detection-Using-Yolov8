
# Fruit Detection Using YOLOv8

## Overview

This project leverages YOLOv8 (You Only Look Once version 8) to detect fruits in images. It includes a frontend application, `app.py`, which allows users to upload images and view the detection results interactively.

## Features

- **Fruit Detection**: Identifies and classifies fruits in images using YOLOv8.
- **Interactive Frontend**: The `app.py` file provides a user-friendly interface to display detection results.
- **Dataset**: Contains images and annotations for model training and evaluation.

## Getting Started

### Prerequisites

- Python 3.x
- Ensure all required Python packages are installed (see `requirements.txt` for a list).

### Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YourGitHubUsername/Fruit-Detection-Using-YOLOv8.git
   cd Fruit-Detection-Using-YOLOv8
Prepare the Dataset

Download the dataset from Kaggle and place it in the appropriate directory.

Run the Application

Start the application by running:

bash
Copy code
python app.py
This will launch the web application, allowing you to upload images and view the results of fruit detection.

**View Detected Images**

The frontend will display both the original image and the detected image with fruits highlighted by bounding boxes.
![image](https://github.com/user-attachments/assets/4ed274af-dadf-4444-8205-796f9a7f395a)
![image](https://github.com/user-attachments/assets/9b952f40-196b-4a4d-8fe7-2fc0d4b3344c)


**Files**
app.py: The main Python file for the frontend application.
requirements.txt: Lists the Python packages required for the project.
dataset/: Directory for the dataset downloaded from Kaggle.
detected_images/: Directory for saving images with detection results.
Dataset
The dataset for this project can be downloaded from Kaggle. It includes images and annotations used for training and testing the YOLOv8 model.

Contributing
Contributions are welcome! To contribute:

**Fork the repository.**
Create a new branch for your changes.
Commit your changes and push to your fork.
Submit a pull request.
For issues or feature requests, open an issue on GitHub.


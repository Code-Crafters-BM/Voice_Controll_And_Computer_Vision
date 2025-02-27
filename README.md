# Voice Control and Computer Vision

## Overview
This repository contains implementations of hand tracking and volume control using computer vision and voice control techniques. The project leverages OpenCV and MediaPipe for real-time hand tracking and gesture recognition.

## Contents

### 1. Hand Tracking Module (`HandTrackingModule.ipynb`)
This Jupyter Notebook demonstrates how to track hand movements using the MediaPipe library. It includes the following functionalities:
- Detecting hand landmarks in real-time.
- Identifying finger positions and gestures.
- Visualizing hand tracking results with OpenCV.

#### Requirements:
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- NumPy (`numpy`)

### 2. Volume Control with Hand Gestures (`VolumeHandcontrol.ipynb`)
This Notebook extends the hand tracking module to control the system volume based on hand gestures. It includes:
- Detecting hand movements.
- Calculating the distance between specific fingers to determine the volume level.
- Controlling the system volume dynamically.

#### Requirements:
- `pycaw` (for audio control)
- OpenCV
- MediaPipe

### 3. Example Files (`exemples/`)
This directory contains various Python scripts and images used for testing and implementing different computer vision functionalities:

- `Demande_reservation formation.pdf`: A sample PDF file for OCR testing.
- `exercice.py`: Contains an exercise implementation related to image processing.
- `hist.py`: Computes and displays the histogram of an image.
- `im.webp`, `image.png`: Sample images used in the project.
- `imread_imshow.py`: Reads and displays an image using OpenCV.
- `ocr.py`: Performs OCR (Optical Character Recognition) on a given image.
- `read.py`: Reads an image and displays it.
- `resize.py`: Resizes an image and displays different transformations.
- `seui.py`: Applies thresholding techniques to an image and visualizes results.

## Installation
To run the notebooks, ensure you have the required dependencies installed. You can install them using:
```bash
pip install opencv-python mediapipe numpy pycaw pytesseract pdf2image
```

## Usage
1. Clone the repository:
```bash
git clone https://github.com/Code-Crafters-BM/Voice_Controll_And_Computer_Vision.git
cd Voice_Controll_And_Computer_Vision
```
2. Open Jupyter Notebook:
```bash
jupyter notebook
```
3. Run `HandTrackingModule.ipynb` to test hand tracking.
4. Run `VolumeHandcontrol.ipynb` to test volume control.

## Future Improvements
- Adding voice control functionality.
- Enhancing gesture recognition for additional commands.
- Implementing multi-hand tracking support.

## Contributors
- **Code Crafters Bm** – Project development and implementation.

## Acknowledgments
- Inspired by OpenCV and MediaPipe tutorials.
- Based on computer vision techniques for gesture recognition.

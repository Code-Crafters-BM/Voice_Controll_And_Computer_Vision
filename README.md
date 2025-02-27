# 🎤 Voice Control and 🎯 Computer Vision

## 📌 Overview
This repository showcases implementations of **hand tracking** and **volume control** using **computer vision** and **voice control techniques**. The project leverages **OpenCV** and **MediaPipe** for real-time hand tracking and gesture recognition.

## 📂 Contents

### 🖐 Hand Tracking Module (`HandTrackingModule.ipynb`)
This Jupyter Notebook provides real-time **hand tracking** using the **MediaPipe** library, including:
✅ Detecting hand landmarks in real-time.
✅ Identifying finger positions and gestures.
✅ Visualizing hand tracking results with OpenCV.

#### 🛠 Requirements:
- 🏆 OpenCV (`cv2`)
- 🔥 MediaPipe (`mediapipe`)
- ⚡ NumPy (`numpy`)

### 🔊 Volume Control with Hand Gestures (`VolumeHandcontrol.ipynb`)
This Notebook extends the **hand tracking module** to **control system volume** using hand gestures:
✅ Detecting hand movements.
✅ Calculating finger distances to adjust volume.
✅ Dynamically controlling system volume.

#### 🛠 Requirements:
- 🎚 `pycaw` (for audio control)
- 🏆 OpenCV
- 🔥 MediaPipe

### 📁 Example Files (`exemples/`)
This directory contains various **Python scripts** and **images** for testing and implementing different **computer vision functionalities**:

📄 **PDF File**
- 📌 `Demande_reservation formation.pdf`: Sample PDF for OCR testing.

📝 **Python Scripts**
- 🏗 `exercice.py`: Implements an exercise related to image processing.
- 📊 `hist.py`: Computes and displays an image histogram.
- 🖼 `imread_imshow.py`: Reads and displays an image using OpenCV.
- 🔍 `ocr.py`: Performs OCR (Optical Character Recognition) on an image.
- 📜 `read.py`: Reads and displays an image.
- 🔄 `resize.py`: Resizes an image with transformations.
- 🖼 `seui.py`: Applies **thresholding techniques** to an image and visualizes results.

🖼 **Sample Images**
- 🖼 `im.webp`, `image.png`: Sample images used in the project.

## 🏗 Installation
To run the notebooks, install the required dependencies using:
```bash
pip install opencv-python mediapipe numpy pycaw pytesseract pdf2image
```

## 🚀 Usage
1️⃣ Clone the repository:
```bash
git clone https://github.com/Code-Crafters-BM/Voice_Controll_And_Computer_Vision.git
cd Voice_Controll_And_Computer_Vision
```
2️⃣ Open Jupyter Notebook: ( Or navigate on your browerser to google collab : https://colab.research.google.com/ ) 
```bash
jupyter notebook
```
3️⃣ Run **`HandTrackingModule.ipynb`** to test hand tracking.
4️⃣ Run **`VolumeHandcontrol.ipynb`** to test volume control.

## 🤝 Contributors
- **Code Crafters Bm** – **Project development and implementation.**

## 💡 Acknowledgments
- 🎓 Inspired by **OpenCV** and **MediaPipe tutorials**.
- 🖥 Based on **computer vision techniques** for **gesture recognition**.


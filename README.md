# 🧠 OpenCV 4.12.0 Projects – Python 3.12 | Ubuntu 24.04 LTS

This repository contains my personal OpenCV experiments and learning projects using **Python 3.12** and **OpenCV 4.12.0** on **Ubuntu 24.04 LTS**.

---

## 📌 About

I’m learning image and video processing with OpenCV. This repo includes basic examples such as:

- Image resizing (with different interpolation methods)
- Morphological operations (erosion, dilation, opening, closing)
- Color conversions (BGR, Grayscale, HSV)
- Real-time video processing with webcam
- Basic object detection techniques

---

## ⚙️ Environment

- 🐍 Python 3.12  
- 📷 OpenCV 4.12.0 (`opencv-python`)  
- 🧮 NumPy  
- 🖼️ Matplotlib (optional for visualization)

---

## 🔧 Installation

### 1. Clone the repo

git clone https://github.com/NightBirdNY/opencv-learning.git
cd opencv-learning

### 2. (Optional) Create a virtual environment

python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies

pip install opencv-python numpy matplotlib

---

## ▶️ Running an Example

python image_resize.py

> Make sure to place test images (e.g. cat1.jpeg) in the "Photos/" folder.

---

## 🧪 Example Scripts

| File              | Description                                               |
|-------------------|-----------------------------------------------------------|
| image_resize.py   | Resize an image using custom rescaleFrame()              |
| morphology.py     | Demonstrates erosion, dilation, opening, and closing     |
| color_space.py    | Converts images to grayscale and HSV color spaces        |
| webcam_demo.py    | Captures real-time video from webcam and processes frames|

---

## 📷 Screenshot / Sample Output

_You can add sample images or before-after comparisons here._

---

## 🎯 Learning Goals

- Learn how OpenCV handles images and pixels
- Understand the effect of different interpolation techniques
- Apply morphological operations to clean or enhance images
- Work with real-time video streams using OpenCV

---

## 💻 System Info

- OS: Ubuntu 24.04 LTS
- Python: 3.12.x
- OpenCV: 4.12.0

---

## ✍️ Author

**NightBirdNY**  
GitHub: https://github.com/NightBirdNY

---

## 📜 License

MIT License

Feel free to use, learn, and contribute!

---

⭐️ If this repository helped you or you find it useful, please consider giving it a star!

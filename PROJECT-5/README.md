# 😊 Real-Time Emotion Detection

A real-time facial emotion detection system built with **OpenCV** and a pre-trained **Keras deep learning model**. It detects faces through your webcam and classifies the emotion displayed — all running locally without any cloud API.

---

## 🎯 What It Does

- Opens your webcam in real time
- Detects faces using Haar Cascade (OpenCV)
- Crops each face, preprocesses it, and feeds it to a CNN model
- Predicts one of **7 emotions** and overlays the label on screen live

### Detectable Emotions
| Label | Label | Label |
|---|---|---|
| 😠 Angry | 🤢 Disgust | 😨 Fear |
| 😄 Happy | 😢 Sad | 😲 Surprise |
| 😐 Neutral | | |

---

## 📁 Project Structure

```
├── emotion_detection.py                 # Main script
├── emotion_model.hdf5                   # Pre-trained Keras CNN model
├── haarcascade_frontalface_default.xml  # OpenCV face detector
└── README.md
```

---

## ⚙️ Requirements

- Python 3.8+
- OpenCV
- NumPy
- TensorFlow / Keras

Install all dependencies with:

```bash
pip install opencv-python numpy tensorflow
```

---

## 🚀 How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

**2. Make sure all three files are in the same folder:**
- `emotion_detection.py`
- `emotion_model.hdf5`
- `haarcascade_frontalface_default.xml`

**3. Run the script:**

On Windows:
```bash
py emotion_detection.py
```

On Mac/Linux:
```bash
python3 emotion_detection.py
```

**4. Press `q` to quit the webcam window.**

---

## 🧠 How It Works

```
Webcam Frame
     │
     ▼
Convert to Grayscale
     │
     ▼
Haar Cascade → Detect Face(s)
     │
     ▼
Crop face ROI → Resize to 64×64
     │
     ▼
Normalize pixel values (÷ 255)
     │
     ▼
Reshape to (1, 64, 64, 1)
     │
     ▼
CNN Model (emotion_model.hdf5) → Predict emotion
     │
     ▼
Draw rectangle + emotion label on frame
     │
     ▼
Display with cv2.imshow()
```

---

## 📌 Notes

- The script uses `cv2.CAP_AVFOUNDATION` by default (Mac). If you're on **Windows**, change this line in `emotion_detection.py`:
  ```python
  # Mac
  cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

  # Windows — use this instead
  cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
  ```
- The model expects **grayscale 64×64** face images as input
- Emotion accuracy depends on lighting and camera angle — good lighting gives better results

---

## 🛠️ Built With

- [OpenCV](https://opencv.org/) — face detection & webcam access
- [Keras / TensorFlow](https://keras.io/) — loading and running the CNN model
- [NumPy](https://numpy.org/) — image array preprocessing
- Pre-trained model trained on the [FER-2013](https://www.kaggle.com/datasets/msambare/fer2013) dataset (7 emotion classes)

---

## 👤 Author

**Bubai De**  
B.Sc (Computer Science) · Haldia Institute of Management  


---

*Part of the Ardent AI/ML Workshop project series*

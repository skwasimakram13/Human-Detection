# Human & Face Detection System

This project is a **Human & Face Detection System** using **YOLO (You Only Look Once)** and **Haarcascade** models in OpenCV with **PyQt5** for the GUI and **Pygame** for audio alerts.

## Features
- **Real-time Human Detection** using YOLOv3.
- **Face Detection every 10 seconds** using Haarcascade.
- **Plays an alert sound** when a human or face is detected.
- **Graphical User Interface (GUI)** built with PyQt5.
- **Start/Stop Camera** controls.

## Installation

### 1. Clone the Repository
```bash
 git clone https://github.com/skwasimakram13/human-detection.git
 cd human-detection
```

### 2. Install Dependencies
Ensure you have Python **3.12+** installed. Then, run:
```bash
pip install -r requirements.txt
```

### 3. Required Files
Place the following files in the project directory:
- `yolov3.cfg` [Download](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg)
- `yolov3.weights` [Download](https://github.com/patrick013/Object-Detection---Yolov3/blob/master/model/yolov3.weights)
- `haarcascade_frontalface_default.xml` [Download](https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml)
- `facevoice.mp3`

### 4. Run the Application
```bash
python human_detection.py
```

## Building an Executable (.exe)
To create a standalone Windows executable, use **PyInstaller**:
```bash
pyinstaller --onefile --windowed --icon="app.ico" \
  --add-data="yolov3.cfg;." \
  --add-data="yolov3.weights;." \
  --add-data="haarcascade_frontalface_default.xml;." \
  --add-data="shop.mp3;." \
  human_detection.py
```
This will generate the `.exe` file inside the `dist/` folder.

## Usage
- **Start Camera**: Click the "Start Camera" button to begin detection.
- **Stop Camera**: Click "Stop Camera" to stop the feed.
- The system will **detect humans in real-time** and **scan for faces every 10 seconds**.
- If detection occurs, **an alert sound (shop.mp3) will play**.

## Requirements
- Python 3.12+
- OpenCV
- NumPy
- PyQt5
- Pygame

## License
This project is licensed under the MIT License.

## Author
**Develope By** - [Sk Wasim Akram](https://github.com/skwasimakram13)


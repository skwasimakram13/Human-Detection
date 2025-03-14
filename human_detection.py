import os
import sys
import cv2
import numpy as np
import pygame
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer

def resource_path(relative_path):
    """ Get absolute path to resource, works for development and PyInstaller EXE """
    if getattr(sys, 'frozen', False):  # If running as an EXE
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(base_path, relative_path)

class HumanDetectionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        # Load YOLO Model
        self.net = cv2.dnn.readNet(resource_path("yolov3.weights"), resource_path("yolov3.cfg"))
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i - 1] for i in self.net.getUnconnectedOutLayers().flatten()]
        self.classes = ["person"]

        # Load Face Detection Model (Haarcascade)
        self.face_cascade = cv2.CascadeClassifier(resource_path("haarcascade_frontalface_default.xml"))

        # Initialize Camera
        self.cap = cv2.VideoCapture(0)
        
        # Timers
        self.video_timer = QTimer(self)  # Timer for video frames
        self.video_timer.timeout.connect(self.update_frame)

        self.face_timer = QTimer(self)  # Timer for face detection (every 10 seconds)
        self.face_timer.timeout.connect(self.detect_faces)
        self.face_timer.start(10000)  # Runs every 10 seconds
        
        # Initialize Pygame for Audio
        pygame.mixer.init()
        
        self.human_detected = False
        self.face_detected = False
        
    def initUI(self):
        """Initialize the GUI layout."""
        self.setWindowTitle("Human & Face Detection System")
        self.setGeometry(100, 100, 800, 600)

        # Video Label
        self.video_label = QLabel(self)
        
        # Start Button
        self.start_button = QPushButton("Start Camera", self)
        self.start_button.clicked.connect(self.start_camera)
        
        # Stop Button
        self.stop_button = QPushButton("Stop Camera", self)
        self.stop_button.clicked.connect(self.stop_camera)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)
    
    def start_camera(self):
        """Start the camera and update frames."""
        self.video_timer.start(30)  # Update every 30ms for smooth video
    
    def stop_camera(self):
        """Stop the camera."""
        self.video_timer.stop()
        self.cap.release()
    
    def detect_faces(self):
        """Run face detection every 10 seconds."""
        ret, frame = self.cap.read()
        if not ret:
            return

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        self.face_detected = len(faces) > 0
        
        if self.face_detected:
            print("Face detected!")

    def update_frame(self):
        """Capture frames from camera, process them, and update the GUI."""
        ret, frame = self.cap.read()
        if not ret:
            return
        
        # Human Detection (YOLO)
        height, width, _ = frame.shape
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outputs = self.net.forward(self.output_layers)
        
        self.human_detected = False
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                if confidence > 0.5 and class_id == 0:  # Class ID 0 is 'person'
                    self.human_detected = True
                    break  # Exit loop once a human is found
        
        # Play audio only if human or face detected
        if self.human_detected or self.face_detected:
            if not pygame.mixer.music.get_busy():  # Play audio only if not already playing
                pygame.mixer.music.load(resource_path("facevoice.mp3"))
                pygame.mixer.music.play()
        
        # Convert frame to QImage
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        qimg = QImage(frame.data, w, h, ch * w, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(qimg))

    def closeEvent(self, event):
        """Release camera on close."""
        self.cap.release()
        event.accept()

# Run the Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HumanDetectionApp()
    window.show()
    sys.exit(app.exec_())

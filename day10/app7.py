# pip install ultralytics
import ultralytics
from ultralytics import YOLO
import cv2

ultralytics.checks()

model = YOLO("yolov8n.pt")
print(f"Model Architecture Task: {model.task}")

results = model("road.jpg")
print("Inference step complete.")
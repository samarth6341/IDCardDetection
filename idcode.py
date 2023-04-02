from ultralytics import YOLO
import numpy

model=YOLO("C:/Users/samar/Downloads/weights (1)/runs/detect/train/weights/last.pt")

detection_output=model.predict(source=0,conf=0.25,save=False,show=True)

#print(detection_output)
print(detection_output[0].numpy)

print(detection_output)






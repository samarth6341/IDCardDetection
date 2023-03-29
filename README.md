# IDCardDetection
This is a custom object detection model that can detect ID cards using the YOLOv8 architecture. The model has been trained on a custom dataset of ID card images.

## Dataset
The custom dataset used to train the model consists of images of ID cards from different countries, with varying backgrounds, orientations, and lighting conditions. The dataset was annotated using the Roboflow Annotation tool to mark the regions of interest (ROIs) for each ID card in the images. 

## Training

The training was done using the annotated data on Roboflows Colab notebook. The output model achieved a 85% Mean Average Precision.




![download](https://user-images.githubusercontent.com/99131011/228625933-d36565b3-f540-490e-9586-4b4be92c9ec7.png)


## Deployment
We can use the id.py file to run the inference on a live webcam feed. 

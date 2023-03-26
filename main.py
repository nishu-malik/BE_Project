print("project started")
#  importing libraries
import cv2
import numpy as np
import gtts
import pyttsx3
from playsound import playsound
# setting the yolo weights and config file
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
# importing the classes from classes file and adding in classes array
classes = []
objectDetected = []
with open("classes.txt", "r") as f:
    classes = f.read().splitlines()

# setting for video capture or camera
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(100, 3))

# starting the capturing of image from video
while True:
    _, img = cap.read()
    height, width, _ = img.shape

    blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.6:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            objectDetected.append(label)
            print(label)
            engine = pyttsx3.init()
            # convert this text to speech
            engine.say(label)
            # play the speech
            engine.runAndWait()
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label + " " + confidence, (x, y + 20), font, 2, (255, 255, 255), 2)

        cv2.imshow('Image', img)
        key = cv2.waitKey(1)
        if key == 's':
            break
print(objectDetected)
cap.release()
cv2.destroyAllWindows()


# Python program to translate
# speech to text and text to speech


# # initialize Text-to-speech engine
# engine = pyttsx3.init()
# # convert this text to speech
# print("hello audio file")
# text = "Python is a great programming language"
# engine.say(text)
# # play the speech
# engine.runAndWait()

print("project finished")
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# ✅ Absolute path fix
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, 'images')

images = []
classNames = []

if not os.path.exists(path):
    print(f"ERROR: Folder not found: {path}")
    exit()

valid_ext = ('.jpg', '.jpeg', '.png', '.bmp')
myList = [f for f in os.listdir(path) if f.lower().endswith(valid_ext)]
print(f"Images found: {myList}")

for cl in myList:
    curImg = cv2.imread(os.path.join(path, cl))
    if curImg is None:
        print(f"Failed to load: {cl}")
        continue
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        if encodings:
            encodeList.append(encodings[0])
        else:
            print("No face detected in one image, skipping.")
    return encodeList

def markAttendance(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []

        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime("%d/%m/%Y,%H:%M:%S")
            f.writelines(f'\n{name},{dtString}')

encodeListKnown = findEncodings(images)
print(f'Encoding Complete — {len(encodeListKnown)} face(s) loaded')

if not encodeListKnown:
    print("ERROR: No faces encoded. Add valid face images to the folder.")
    exit()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("ERROR: Cannot open webcam.")
    exit()

while True:
    success, img = cap.read()
    if not success:
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            top, right, bottom, left = faceLoc
            top, right, bottom, left = top*4, right*4, bottom*4, left*4

            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(img, (left, bottom-35), (right, bottom), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (left+6, bottom-6),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
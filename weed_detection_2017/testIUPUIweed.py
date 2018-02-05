import numpy as np
import cv2
import time
import serial

#integrated 2 camera feed
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#face_cascade = cv2.CascadeClassifier('Haarweed1.xml')

#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#nose_cascade = cv2.CascadeClassifier('haarcascade_nose.xml')


cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)

ser = serial.Serial('COM3', 19200,timeout=5)
time.sleep(6)
print(ser)

detected=False

while True:

#CAMERA 1-right hand side camera facing Agbot from front
    ret1, img1 = cap1.read()

    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    #nose = nose_cascade.detectMultiScale(gray, 1.3, 5)

    for (x1, y1, w1, h1) in faces:
        cv2.rectangle(img1, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 2)
        cv2.putText(img1, "Weed", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    if faces == ():
        pass
    else:
        detect_face1 = x1
        print 'weed distance CAM RHS ', detect_face1
        if 50 < detect_face1 < 150:
            if detected:
                pass
            else:
                print '1'
                ser.write('1')
                detected = True
        else:
            if detected:
                print'2'
                ser.write('2')
                detected = False
            else:
                pass


# For CAMERA 2-left hand side camera facing Agbot from front

    ret2, img2 = cap2.read()

    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    #nose = nose_cascade.detectMultiScale(gray, 1.3, 5)

    for (x21, y21, w21, h21) in faces:
        cv2.rectangle(img2, (x21, y21), (x21 + w21, y21 + h21), (255, 0, 0), 2)
        cv2.putText(img2, "Weed", (x21, y21), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    if faces == ():
        pass
    else:
        detect_face21 = x21
        print 'weed distance CAM LHS ', detect_face21
        if 50 < detect_face21 < 150:
            if detected:
                pass
            else:
                print '7'
                ser.write('7')
                detected = True
        else:
            if detected:
                print'8'
                ser.write('8')
                detected = False
            else:
                pass

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
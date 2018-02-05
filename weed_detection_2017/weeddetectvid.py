import numpy as np
import cv2
import serial
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

nose_cascade = cv2.CascadeClassifier('haarcascade_nose.xml')



cap = cv2.VideoCapture(0)

ser = serial.Serial('COM1', 19200,timeout=5)
time.sleep(6)
print(ser)

detected=False

while 1:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    eyes= eye_cascade.detectMultiScale(gray, 1.3, 5)

    nose = nose_cascade.detectMultiScale(gray, 1.3, 5)

    for (x1, y1, w1, h1) in faces:
        cv2.rectangle(img, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 2)

        if x1 > 0:
            cv2.putText(img, "Face", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff

    detect_face = x1

    print 'face distance: ', detect_face
    if 80 < detect_face < 100:
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

    if k == 27:
        break

    for (x2, y2, w2, h2) in nose:
        cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)
        if x2 > 0:
            cv2.putText(img, "Nose", (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff

    detect_nose = x2

    print 'nose distance: ', detect_nose
    if 80 < detect_nose < 100:
        if detected:
            pass
        else:
            print '3'
            ser.write('3')
            detected = True
    else:
        if detected:
            print'4'
            ser.write('4')
            detected = False
        else:
            pass

    if k == 27:
        break

    for (x3, y3, w3, h3) in eyes:
        cv2.rectangle(img, (x3, y3), (x3 + w3, y3 + h3), (255, 0, 0), 2)

    if x3 > 0:
        cv2.putText(img, "Eye", (x3, y3), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 2, cv2.LINE_AA)

    detect_eye=x3
    print 'eye distance: ', detect_eye
    if 80 < detect_nose < 100:
        if detected:
            pass
        else:
            print '5'
            ser.write('5')
            detected = True
    else:
        if detected:
            print'6'
            ser.write('6')
            detected = False
        else:
            pass

    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
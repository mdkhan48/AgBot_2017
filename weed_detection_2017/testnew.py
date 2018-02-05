import numpy as np
import cv2
import time


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

nose_cascade = cv2.CascadeClassifier('haarcascade_nose.xml')


cap1 = cv2.VideoCapture(0)
#cap2 = cv2.VideoCapture(2)

detected=False

while True:


    ret1, img1 = cap1.read()

    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    nose = nose_cascade.detectMultiScale(gray, 1.3, 5)

    print (faces)

    for (x1, y1, w1, h1) in faces:
        cv2.rectangle(img1, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 2)
        cv2.putText(img1, "Face", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    #detect_face1 = x1

    #print 'face distance Camera 1: ', detect_face1
    if faces == ():
        pass
    else:
        detect_face1 = x1
        print 'face distance ', detect_face1
        if 50 < detect_face1 < 150:
            if detected:
                pass
            else:
                print '1'
                detected = True
        else:
            if detected:
                print'2'
                # ser.write('2')
                detected = False
            else:
                pass


    '''for (x2, y2, w2, h2) in nose:
        cv2.rectangle(img1, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)
    if x2 > 0:
        cv2.putText(img1, "Nose", (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)'''

    '''for (x3, y3, w3, h3) in eyes:
        cv2.rectangle(img1, (x3, y3), (x3 + w3, y3 + h3), (255, 0, 0), 2)

        if x3 > 0:
            cv2.putText(img1, "Eye", (x3, y3), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255), 2, cv2.LINE_AA)'''


    cv2.imshow('img', img1)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break




    '''ret2, img2 = cap2.read()

    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    nose = nose_cascade.detectMultiScale(gray, 1.3, 5)

    for (x21, y21, w21, h21) in faces:
        cv2.rectangle(img2, (x21, y21), (x21 + w21, y21 + h21), (255, 0, 0), 2)
        cv2.putText(img2, "Face", (x21, y21), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    for (x22, y22, w22, h22) in nose:
        cv2.rectangle(img2, (x22, y22), (x22 + w22, y22 + h22), (255, 0, 0), 2)
        if x22 > 0:
            cv2.putText(img2, "Nose", (x22, y22), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    for (x23, y23, w23, h23) in eyes:
        cv2.rectangle(img2, (x23, y23), (x23 + w23, y23 + h23), (255, 0, 0), 2)

        if x3 > 0:
            cv2.putText(img2, "Eye", (x23, y23), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('img2', img2)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break



    #cv2.imshow('img1', img1)
    #cv2.imshow('img2', img2)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break'''

cap1.release()
#cap2.release()
cv2.destroyAllWindows()
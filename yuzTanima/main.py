# OpenCV ile Yüz Tanıma
# OpenCV kütüphanesi yoksa yükleyin
# photos klasörüne test.mp4 isminde bir video ekleyin

# Videoda bahsedilen hazır Classifier dosyası indirmek için:
# https://github.com/opencv/opencv/tree/master/data/haarcascades

# Kendi Classifier dosyamızı oluşturabildiğimiz Cascade Trainer programını indirmek için:
# https://amin-ahmadi.com/cascade-trainer-gui/

import cv2

face_cascade = cv2.CascadeClassifier(
    r"classifier/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(r"photos/test.mp4")
while cap.isOpened():
    _,img = cap.read()

    #img = cv2.imread(r"photos/1588088785877.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),3)

    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()





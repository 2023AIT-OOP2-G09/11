import cv2

img_path = 'sample.png'
img = cv2.imread(img_path)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image, 1.1, 3)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.imwrite('Detected_Faces.png', img)

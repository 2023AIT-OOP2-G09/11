import cv2
import urllib
import numpy as np

# ウェブでアップロードされた画像を受け取る
image_url = "hiroy.jpg"
image = cv2.imread(image_url)


# grayscale変換
image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 画像から人の顔を認識
face_check = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
faces = face_check.detectMultiScale(
    image_grayscale, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30)
)

# 顔を認識したらモザイクをかける
for x, y, w, h in faces:
    face_region = image[y : y + h, x : x + w]
    face_mozaic = cv2.resize(
        face_region, (w // 10, h // 10), interpolation=cv2.INTER_NEAREST
    )
    face_mozaic = cv2.resize(face_mozaic, (w, h), interpolation=cv2.INTER_NEAREST)
    image[y : y + h, x : x + w] = face_mozaic

# モザイクをかけた画像を保存
cv2.imwrite("image/result.jpg", image)

cv2.imshow("image/result.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

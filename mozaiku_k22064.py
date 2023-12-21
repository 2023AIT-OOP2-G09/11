import cv2
import urllib
import numpy as np

# ウェブでアップロードされた画像を受け取る
image_url = "画像のURL"

response = urllib.request.urlopen(image_url)
img_array = np.array(bytearray(response.read()), dtype=np.uint8)
image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
# grayscale変換
image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 画像から人の顔を認識
face_check = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontal_default.xml"
)
face = face_check.detectMultiScale(
    image_grayscale, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30)
)

# 顔を認識したらモザイクをかける
for x, y, w, h in face:
    face = image[y : y + h, x : x + w]
    face = cv2.resize(face, (w // 10, h // 10), interpolation=cv2.INPAINT_NEAREST)
    face = cv2.resize(face, (w, h), interpolation=cv2.INPAINT_NEAREST)
    image[y : y + h, x : x + w] = face

# モザイクをかけた画像を保存
cv2.imwrite("image/result.jpg", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# 顔にモザイクをかける関数
def apply_mosaic_to_faces(image_path, output_path="output_image/mozaiku.jpg"):
    # 画像を読み込む
    image = cv2.imread(image_path)

    # grayscale変換
    image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 画像から人の顔を認識
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(image_grayscale, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # 顔を認識したらモザイクをかける
    for x, y, w, h in faces:
        face_region = image[y : y + h, x : x + w]
        face_mozaic = cv2.resize(face_region, (w // 10, h // 10), interpolation=cv2.INTER_NEAREST)
        face_mozaic = cv2.resize(face_mozaic, (w, h), interpolation=cv2.INTER_NEAREST)
        image[y : y + h, x : x + w] = face_mozaic

    # モザイクをかけた画像を保存
    cv2.imwrite(output_path, image)

    # 画像を表示
    cv2.imshow("Mosaic Applied Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 画像のパスを指定して関数を呼び出す
image_path = "uploads/hiroy.jpg"
apply_mosaic_to_faces(image_path)

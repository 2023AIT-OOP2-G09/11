import cv2

def detect_and_draw_faces(image_path, output_path='output_image/Detected_Faces.png'):
    # 画像を読み込む
    img = cv2.imread(image_path)

    # グレースケール化
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 顔検出用の分類器を読み込む
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

    # 顔を検出
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=3)

    # 検出された顔に枠を描く
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # 結果を表示
    cv2.imshow('Detected Faces', img)
    cv2.waitKey(0)

    # 画像を保存
    cv2.imwrite(output_path, img)

# 画像のパスを指定して関数を呼び出す
image_path = 'uploads/hiroy.jpg'
detect_and_draw_faces(image_path)
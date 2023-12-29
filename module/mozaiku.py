import cv2
import os

def apply_mosaic_to_faces(input_image_path):
    # 画像を読み込む
    image = cv2.imread(input_image_path)

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

    # 保存先ディレクトリの作成
    output_dir = 'mozaiku_image'
    os.makedirs(output_dir, exist_ok=True)

    # 名前をつけて保存
    out_filename = os.path.basename(input_image_path)

    # 出力ファイルパス
    output_path = os.path.join(output_dir, out_filename)

    # モザイクをかけた画像を保存
    cv2.imwrite(output_path, image)
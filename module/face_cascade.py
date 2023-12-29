import os
import cv2

def detect_and_draw_faces(input_image_path):
    # 画像を読み込む
    img = cv2.imread(input_image_path)

    # グレースケール化
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 顔検出用の分類器を読み込む
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

    # 顔を検出
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=3)

    # 検出された顔に枠を描く
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # 保存先ディレクトリの作成
    output_dir = 'cascade_image'
    os.makedirs(output_dir, exist_ok=True)

    # 名前をつけて保存
    out_filename = os.path.basename(input_image_path)

    # 出力ファイルパス
    output_path = os.path.join(output_dir, out_filename)

    # 画像を保存
    cv2.imwrite(output_path, img)
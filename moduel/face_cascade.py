import cv2
import os

def process_images(input_folder, output_folder):
    # 出力フォルダが存在しない場合は作成
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # input_folder内のすべての画像ファイルに処理を適用
    for filename in os.listdir(input_folder):
        input_image_path = os.path.join(input_folder, filename)

        # 画像処理の関数を呼び出し
        detect_and_draw_faces(input_image_path, os.path.join(output_folder, filename))

# アップロードされた画像の保存先ディレクトリ
UPLOAD_FOLDER = 'uploads'

# 処理済み画像の保存先ディレクトリ
PROCESSED_FOLDER = 'face_cascade_image'

def detect_and_draw_faces(input_image_path, output_path):
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

    # 結果を表示
    #cv2.imshow('Detected Faces', img)
    #cv2.waitKey(0)

    # 画像を保存
    cv2.imwrite(output_path, img)

if __name__ == "__main__":
    # アップロードされた画像の処理
    process_images(UPLOAD_FOLDER, PROCESSED_FOLDER)
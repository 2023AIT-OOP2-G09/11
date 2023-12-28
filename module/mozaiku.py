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
        apply_mosaic_to_faces(input_image_path, os.path.join(output_folder, filename))

# アップロードされた画像の保存先ディレクトリ
UPLOAD_FOLDER = 'uploads'

# 処理済み画像の保存先ディレクトリ
PROCESSED_FOLDER = 'mozaiku_image'


# 顔にモザイクをかける関数
def apply_mosaic_to_faces(input_image_path, output_path):
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

    # モザイクをかけた画像を保存
    cv2.imwrite(output_path, image)

    # 画像を表示
    #cv2.imshow("Mosaic Applied Image", image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

if __name__ == "__main__":
    # アップロードされた画像の処理
    process_images(UPLOAD_FOLDER, PROCESSED_FOLDER)

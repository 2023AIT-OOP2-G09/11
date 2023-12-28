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
        grayscale_and_threshold(input_image_path, os.path.join(output_folder, filename))

# アップロードされた画像の保存先ディレクトリ
UPLOAD_FOLDER = 'uploads'

# 処理済み画像の保存先ディレクトリ
PROCESSED_FOLDER = 'grayscale_image'


# 画像処理の関数
def grayscale_and_threshold(input_image_path, output_path):
    # 画像を読み込む
    image = cv2.imread(input_image_path)

    # グレースケール化
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # ここで適切な閾値を設定し、二値化を行う
    _, threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    # 画像の保存
    cv2.imwrite(output_path, threshold_image)

if __name__ == "__main__":
    # アップロードされた画像の処理
    process_images(UPLOAD_FOLDER, PROCESSED_FOLDER)
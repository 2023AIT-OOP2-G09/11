import cv2
import os

def grayscale_and_threshold(input_image_path):
    # 画像を読み込む
    image = cv2.imread(input_image_path)

    # グレースケール化
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # ここで適切な閾値を設定し、二値化を行う
    _, threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    # 保存先ディレクトリの作成
    output_dir = 'grayscale_image'
    os.makedirs(output_dir, exist_ok=True)

    # 名前をつけて保存
    out_filename = os.path.basename(input_image_path)

    # 出力ファイルパス
    output_path = os.path.join(output_dir, out_filename)

    # 画像の保存
    cv2.imwrite(output_path, threshold_image)

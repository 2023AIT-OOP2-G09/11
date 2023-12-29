import os
import cv2

def apply_canny_edge_detection(input_path):
    # 画像の読み込み
    image = cv2.imread(input_path)

    # Cannyエッジ検出の処理（例）
    edges = cv2.Canny(image, 100, 200)

    # 保存先ディレクトリの作成
    output_dir = 'canny_image'
    os.makedirs(output_dir, exist_ok=True)

    # 名前をつけて保存
    out_filename = os.path.basename(input_path)

    # 出力ファイルパス
    output_path = os.path.join(output_dir, out_filename)

    # 画像の保存
    cv2.imwrite(output_path, edges)
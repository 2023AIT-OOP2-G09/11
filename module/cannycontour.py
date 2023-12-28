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
        apply_canny_edge_detection(input_image_path, os.path.join(output_folder, filename))

# アップロードされた画像の保存先ディレクトリ
UPLOAD_FOLDER = 'uploads'

# 処理済み画像の保存先ディレクトリ
PROCESSED_FOLDER = 'canny_image'

def apply_canny_edge_detection(input_image_path, output_path, low_threshold=100, high_threshold=200):
    # 画像を読み込む
    img = cv2.imread(input_image_path)

    # グレースケール化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Cannyエッジ検出を適用
    edges = cv2.Canny(gray, low_threshold, high_threshold)

    # 結果を保存
    cv2.imwrite(output_path, edges)

    # 画像を表示
    #cv2.imshow("Mosaic Applied Image", edges)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

if __name__ == "__main__":
    # アップロードされた画像の処理
    process_images(UPLOAD_FOLDER, PROCESSED_FOLDER)
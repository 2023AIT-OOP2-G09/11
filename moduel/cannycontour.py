import cv2

def apply_canny_edge_detection(input_path, output_path='output_image/canny.jpg', low_threshold=100, high_threshold=200):
    # 画像を読み込む
    img = cv2.imread(input_path)

    # グレースケール化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Cannyエッジ検出を適用
    edges = cv2.Canny(gray, low_threshold, high_threshold)

    # 結果を保存
    cv2.imwrite(output_path, edges)

    # 画像を表示
    cv2.imshow("Mosaic Applied Image", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 関数を呼び出す
input_image_path = "uploads/hiroy.jpg"
apply_canny_edge_detection(input_image_path)

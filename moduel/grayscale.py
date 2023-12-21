import cv2

def grayscale_and_threshold(input_image_path, output_path="output_image/grayscale.jpg"):
    # 画像を読み込む
    image = cv2.imread(input_image_path)

    # グレースケール化
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 画像の確認（グレースケール）
    cv2.imshow('Gray Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # ここで適切な閾値を設定し、二値化を行う
    _, threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    # 画像の保存
    cv2.imwrite(output_path, threshold_image)

    # 画像の確認（二値化）
    cv2.imshow('Threshold Image', threshold_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 画像のパスを指定して関数を呼び出す
input_image_path = 'uploads/images01.jpg'
grayscale_and_threshold(input_image_path)
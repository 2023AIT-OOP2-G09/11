import cv2

def grayscale_and_threshold(input_image_path, output_path):
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

    # 画像の確認（二値化）
    cv2.imshow('Threshold Image', threshold_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 画像の保存
    cv2.imwrite(output_path, threshold_image)

if __name__ == "__main__":
    input_image_path = 'image/images.jpeg'
    output_image_path = 'image/threshold_output.jpg'

    grayscale_and_threshold(input_image_path, output_image_path)
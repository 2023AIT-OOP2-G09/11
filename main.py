from flask import Flask, render_template, request, redirect, url_for,send_from_directory
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from moduel.cannycontour import apply_canny_edge_detection
from moduel.face_cascade import detect_and_draw_faces
from moduel.grayscale import grayscale_and_threshold
from moduel.mozaiku import apply_mosaic_to_faces
import cv2

app = Flask(__name__)

current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_watch = os.path.join(current_dir, 'uploads')


# アップロードされた画像の保存先ディレクトリ
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# アップロードされたファイルが許可された拡張子かどうかを確認する関数
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            # ディレクトリが変更された場合の処理
            print(f'Directory modified: {event.src_path}')
            # ここに実行したいプログラムのコードを追加
            apply_canny_edge_detection()
            detect_and_draw_faces()
            grayscale_and_threshold()
            apply_mosaic_to_faces()

# Flaskアプリケーション外でObserverオブジェクトを生成
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=path_to_watch, recursive=True)


@app.route('/')
def index():
    #path_to_watch = 'uploads'

    #event_handler = MyHandler()
    #observer = Observer()
    #observer.schedule(event_handler, path=path_to_watch, recursive=True)

    print(f"Watching directory: {path_to_watch}")

    #try:
        # 監視を開始
    #    observer.start()
    #    while True:
    #        time.sleep(1)
    #except KeyboardInterrupt:
        # Ctrl+Cが押されたら終了
    #    observer.stop()
    #observer.join()
    return render_template('index.html')
   
@app.route('/upload', methods=['POST'])
def upload_file():
    # フォームから送信されたファイルを取得
    file = request.files['file']

    # ファイルが選択されていない場合の処理
    if file.filename == '':
        return redirect(request.url)

    # ファイルの拡張子が許可されたものかどうかを確認
    if file and allowed_file(file.filename):
        # アップロードされたファイルを保存する
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # 成功時の処理
        message = f'{file.filename} が正常にアップロードされました。'
        return render_template('index.html', message=message)

    # 許可されていない拡張子の場合の処理
    return '許可されていないファイル形式です。'

@app.route('/applist')
def applist():
    # uploadsディレクトリ内の画像ファイル名を取得
    filenames = [filename for filename in os.listdir(os.path.join(current_dir, 'uploads')) if allowed_file(filename)]
    return render_template('applist_form.html', filenames=filenames)

@app.route('/apppic/<filename>')
def app_pic(filename):
    # uploads ディレクトリから画像を返す
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# 処理済み画像の保存先ディレクトリ
PROCESSED_FOLDER_GRAY = 'grayscale_image'
app.config['PROCESSED_FOLDER_GRAY'] = PROCESSED_FOLDER_GRAY 

@app.route('/gray')
def gray():
    # grayscale_image ディレクトリ内の画像ファイル名を取得
    gray_dir = os.path.join(current_dir, PROCESSED_FOLDER_GRAY)
    filenames = [filename for filename in os.listdir(os.path.join(current_dir, 'grayscale_image')) if allowed_file(filename)]
    return render_template('grayscale_form.html', filenames=filenames)

@app.route('/graypic/<filename>')
def gray_pic(filename):
    # grayscale_img ディレクトリから画像を返す
    return send_from_directory(app.config['PROCESSED_FOLDER_GRAY'], filename)

# 処理済み画像の保存先ディレクトリ
PROCESSED_FOLDER_MOZAIKU = 'mozaiku_image'
app.config['PROCESSED_FOLDER_MOZAIKU'] = PROCESSED_FOLDER_MOZAIKU 

@app.route('/mozaiku')
def mozaiku():
    # grayscale_image ディレクトリ内の画像ファイル名を取得
    mozaiku_dir = os.path.join(current_dir, PROCESSED_FOLDER_MOZAIKU)
    filenames = [filename for filename in os.listdir(os.path.join(current_dir, 'mozaiku_image')) if allowed_file(filename)]
    return render_template('mozaiku_form.html', filenames=filenames)

@app.route('/mozaikupic/<filename>')
def mozaiku_pic(filename):
    # grayscale_img ディレクトリから画像を返す
    return send_from_directory(app.config['PROCESSED_FOLDER_MOZAIKU'], filename)

# 処理済み画像の保存先ディレクトリ
PROCESSED_FOLDER_CASCADE = 'CASCADE_image'
app.config['PROCESSED_FOLDER_CASCADE'] = PROCESSED_FOLDER_CASCADE

@app.route('/cascade')
def cascade():
    # grayscale_image ディレクトリ内の画像ファイル名を取得
    cascade_dir = os.path.join(current_dir, PROCESSED_FOLDER_CASCADE)
    filenames = [filename for filename in os.listdir(os.path.join(current_dir, 'cascade_image')) if allowed_file(filename)]
    return render_template('cascade_form.html', filenames=filenames)

@app.route('/cascadepic/<filename>')
def cascade_pic(filename):
    # grayscale_img ディレクトリから画像を返す
    return send_from_directory(app.config['PROCESSED_FOLDER_CASCADE'], filename)

# 処理済み画像の保存先ディレクトリ
PROCESSED_FOLDER_CANNY = 'canny_image'
app.config['PROCESSED_FOLDER_CANNY'] = PROCESSED_FOLDER_CANNY 

@app.route('/canny')
def canny():
    # grayscale_image ディレクトリ内の画像ファイル名を取得
    canny_dir = os.path.join(current_dir, PROCESSED_FOLDER_CANNY)
    filenames = [filename for filename in os.listdir(os.path.join(current_dir, 'canny_image')) if allowed_file(filename)]
    return render_template('canny_form.html', filenames=filenames)

@app.route('/cannypic/<filename>')
def canny_pic(filename):
    # grayscale_img ディレクトリから画像を返す
    return send_from_directory(app.config['PROCESSED_FOLDER_CANNY'], filename)

#if __name__ == "__main__":
#    app.run(debug=True)
if __name__ == "__main__":
    try:
        # Flaskアプリケーションの起動
        app.run(debug=True, use_reloader=False)
    except KeyboardInterrupt:
        # Ctrl+Cが押されたらObserverを停止
        observer.stop()
    observer.join()
    

from flask import Flask, render_template, request, redirect, url_for
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from moduel.cannycontour import apply_canny_edge_detection
from moduel.face_cascade import detect_and_draw_faces
from moduel.grayscale import grayscale_and_threshold
from moduel.mozaiku_k22064 import apply_mosaic_to_faces
app = Flask(__name__)

# アップロードされた画像の保存先ディレクトリ
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# アップロードされたファイルが許可された拡張子かどうかを確認する関数
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    path_to_watch = '/Users/k22065kk/Documents/GitHub/11/uploads'

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)

    print(f"Watching directory: {path_to_watch}")

    try:
        # 監視を開始
        observer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Ctrl+Cが押されたら終了
        observer.stop()
    observer.join()
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
        return 'ファイルが正常にアップロードされました。'

    # 許可されていない拡張子の場合の処理
    return '許可されていないファイル形式です。'



class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            # ディレクトリが変更された場合の処理
            print(f'Directory modified: {event.src_path}')
            # ここに実行したいプログラムのコードを追加
            apply_canny_edge_detection(UPLOAD_FOLDER)
            detect_and_draw_faces(UPLOAD_FOLDER)
            grayscale_and_threshold(UPLOAD_FOLDER)
            apply_mosaic_to_faces(UPLOAD_FOLDER)
            Canny_FOLDER = 
            app.config['Canny_FOLDER'] = Canny_FOLDER
            Drawface_FOLDER = 
            app.config['drawface_FOLDER'] = Drawface_FOLDER
            Grayscale_FOLDER = 
            app.config['grayscale_FOLDER'] = Grayscale_FOLDER
            Mosaic_FOLDER = 
            app.config['Canny_FOLDER'] = Mosaic_FOLDER
if __name__ == "__main__":
    app.run(debug=True)
    

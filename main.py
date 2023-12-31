from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from pathlib import Path
import os

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

# ホームページ
@app.route('/')
def index():
    print(f"Watching directory: {path_to_watch}")
    return render_template('index.html')

# 画像アップロード処理
@app.route('/upload', methods=['POST'])
def upload_file():
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

# 画像一覧表示
@app.route('/applist')
def applist():
    # uploadsディレクトリ内の画像ファイル名を取得
    filenames = [filename for filename in os.listdir(os.path.join(current_dir, 'uploads')) if allowed_file(filename)]
    return render_template('applist_form.html', filenames=filenames)

# アップロードされた画像の表示
@app.route('/apppic/<filename>')
def app_pic(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# 処理済み画像の保存先ディレクトリ
PROCESSED_FOLDER_GRAY = 'grayscale_image'
app.config['PROCESSED_FOLDER_GRAY'] = PROCESSED_FOLDER_GRAY 

# グレースケール画像表示
@app.route('/gray')
def gray():
    gray_dir = os.path.join(current_dir, PROCESSED_FOLDER_GRAY)
    filenames = [filename for filename in os.listdir(os.path.join(current_dir, 'grayscale_image')) if allowed_file(filename)]
    return render_template('grayscale_form.html', filenames=filenames)

# グレースケール画像の表示
@app.route('/graypic/<filename>')
def gray_pic(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER_GRAY'], filename)

# 処理済み画像の保存先ディレクトリ
PROCESSED_FOLDER_MOZAIKU = 'mozaiku_image'
app.config['PROCESSED_FOLDER_MOZAIKU'] = PROCESSED_FOLDER_MOZAIKU 

# モザイク画像表示
@app.route('/mozaiku')
def mozaiku():
    mozaiku_dir = os.path.join(current_dir, PROCESSED_FOLDER_MOZAIKU)
    filenames = [filename for filename in os.listdir(os.path.join(current_dir, 'mozaiku_image')) if allowed_file(filename)]
    return render_template('mozaiku_form.html', filenames=filenames)

# モザイク画像の表示
@app.route('/mozaikupic/<filename>')
def mozaiku_pic(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER_MOZAIKU'], filename)

# 処理済み画像の保存先ディレクトリ
PROCESSED_FOLDER_CASCADE = 'CASCADE_image'
app.config['PROCESSED_FOLDER_CASCADE'] = PROCESSED_FOLDER_CASCADE

# カスケード画像表示
@app.route('/cascade')
def cascade():
    cascade_dir = os.path.join(current_dir, PROCESSED_FOLDER_CASCADE)
    filenames = [filename for filename in os.listdir(os.path.join(current_dir, 'cascade_image')) if allowed_file(filename)]
    return render_template('cascade_form.html', filenames=filenames)

# カスケード画像の表示
@app.route('/cascadepic/<filename>')
def cascade_pic(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER_CASCADE'], filename)

# 処理済み画像の保存先ディレクトリ
PROCESSED_FOLDER_CANNY = 'canny_image'
app.config['PROCESSED_FOLDER_CANNY'] = PROCESSED_FOLDER_CANNY 

# カニー画像表示
@app.route('/canny')
def canny():
    canny_dir = os.path.join(current_dir, PROCESSED_FOLDER_CANNY)
    filenames = [filename for filename in os.listdir(os.path.join(current_dir, 'canny_image')) if allowed_file(filename)]
    return render_template('canny_form.html', filenames=filenames)

# カニー画像の表示
@app.route('/cannypic/<filename>')
def canny_pic(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER_CANNY'], filename)

# Flaskアプリケーションの起動
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

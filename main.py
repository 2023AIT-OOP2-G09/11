from flask import Flask, render_template, request, redirect, url_for
import os

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

if __name__ == "__main__":
    app.run(debug=True)

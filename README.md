# 11

## 役割分担
| 役割     | 氏名      | 学籍番号     |
| -------------- | -------------- | ----------- |
|トップページ及びファイルのアップロード部分の作成 |藤田勇輝 |k22112 | 
|アップロード画像や処理済み画像の一覧ページの作成 |竹本弥生 |k22083 |
|顔検出してモザイク |柴田翔空 |k22064 |
|顔検出して枠で囲う |村山颯真 |k22135 |
|Carryフィルタによる輪郭抽出 |杉山怜央 |k21069 |
|画像のグレースケール化 (できれば2値化も) |横井聡 |k22144 |
|ディレクトリ監視から各画像処理呼び出しをするプログラム |後藤啓輔 |k22054 |

## システムの動作確認方法
１.ターミナルを二つ別で開き、frask側のプログラムとファイル変更監視プログラムを起動する。
<br>
２.frask側で画像処理をかけたい画像にをアップロードする。
<br>
3.webサイト上で画像処理の種類別に閲覧することができ、処理後の画像がそれぞれのファイルに保存される
<br>
※同じ名前のファイルは受け付けていないので気をつけること


## 使用したライブラリのバージョン
| ライブラリ     | バージョン      |
| -------------- | -------------- |
| tensorflow-macos | 2.15.0 |
| torch | 2.1.1 |
| torchvision | 0.16.1 |
| torchaudio | 2.1.1 |


## ディレクトリの構造
[11]
<br>
  ├[moduel]（画像処理）
<br>
  │  └cannycontor.py
<br>
  │  └face_cascade.py
<br>
  │  └grayscale.py
<br>
  │  └mozaiku.py
<br>
  ├[canny_image]（処理後の画像）
<br>
  ├[cascade_image]（処理後の画像）
<br>
  ├[grayscale_image]（処理後の画像）
<br>
  ├[mozaiku_image]（処理後の画像）
<br>
  ├[templates](webサイトのそれぞれのhtml)
<br>
  │  └index.html
<br>
  │  └applist_form.html
<br>
  │  └canny_form.html
<br>
  │  └cascade.html
<br>
  │  └gratscale_form.html
<br>
  │  └mozaiku.html
<br>
  ├[uploads]（アップロードした画像）
<br>
  │  └hiroy.jpg
<br>
  │  └images01.jpg
<br>
  └main.py (frask側のプログラム)
<br>
  └image_process.py (ファイル変更監視のプログラム)
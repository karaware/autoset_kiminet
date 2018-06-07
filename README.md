# 概要
キミネット様で月毎スケジュール設定変更依頼を半自動化するツールです。  
キミネット様から頂くスケジュールの記載されたexcelファイルを読み込ませることで  
TimeGroupへの設定を自動で行います。（リロードは手動）

# 使い方
### スケジュール設定をexcelから自動設定する
①  
http://adm15.qloog.ne.jp/autoset_kiminet/upload  
上記のURLにアクセス  

②  
「ファイルを選択」をクリックしてキミネット様から頂いたexcelファイルを選択する  

③  
「Excelファイルから設定を実行」をクリックする  

④  
実行したクエリが表示されることを確認  

⑤  
202.78.218.162
キミネット様PBXのGUIにログインして空リロード実施  

※  
- 「スケジュール設定をexcelから自動設定する」機能はexcelの列を固定で判断しているため  
  excelファイルのレイアウトが変わると動作しません。  
- 月の概念はexcelファイルの内容に関わらず自動的に翌月を指定して設定します。  
  つまり、現在が5月で、4月分のスケジュールexcelファイルを読み込ませても  
  各日の設定はexcelファイルの内容を利用して、月は6月で設定します。

### 先月分のスケジュール設定を削除する
①  
http://adm15.qloog.ne.jp/autoset_kiminet/upload  
上記のURLにアクセス  

②  
「先月分削除」をクリックする

③  
実行したクエリが表示されることを確認  

④  
202.78.218.162
キミネット様PBXのGUIにログインして空リロード実施  

# 仕様
言語 : Python3.6.4
Python仮想環境 : pyenv + pyenv-virtualenv
Pythonフレームワーク : Bottle
CSSフレームワーク : BootStrap
動作ホスト : adm15.qloog.ne.jp

# 各ファイル説明
- adapter.wsgi  
  Bottleでapacheを利用するためのファイル

- bottle.py  
  BOttleのライブラリファイル  

- upload.py  
  MVCモデルで言う所の「ルーティング」と「コントローラ」を担う

- index.html  
  MVCモデルで言う所の「ビュー」
  以下のURLのアクセス先のHTML描画を行う
  http://adm15.qloog.ne.jp/autoset_kiminet/upload

- mkexecsql.py  
  excelファイルからPBXに設定を行う
  「Excelファイルから設定を実行」がクリックされた際に呼び出される

- sql.html
  「Excelファイルから設定を実行」がクリックされた際にmkexecsql.pyの処理が終わった後に  
  HTML描画を行う

- rm_prev_month.py  
  先月分のスケジュール設定を削除する  
  「先月分削除」がクリックされた際に呼び出される  

- comp_rm.html  
  先月分削除」がクリックされた際にrm_prev_month.pyの処理が終わった後に  
  HTML描画を行う





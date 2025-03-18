from flask import Flask
from init import app, db
import chatbotBaseAI
import api

def create_app(config_name):
    app = Flask(__name__)

    # 設定の読み込み
    if config_name == 'testing':
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    # 拡張機能の初期化
    db.init_app(app)
    # 他の拡張機能の初期化もここに追加

    # ブループリントの登録
    # app.register_blueprint(api_blueprint)

    return app

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)
    chatbotBaseAI.start_chat()

# デバッグモードTrueにすると変更が即反映される
# ファイルのエンコードはUTF-8で保存すること
# 下記URLをブラウザに打ち込むとページが開く
# http://127.0.0.1:8080/
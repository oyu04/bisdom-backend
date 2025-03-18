from model.models import db, Users, Group, Knowledge, Like
from test_data.knowledge_data1 import test_knowledge

def db_connect(app):
    # 設定ファイルの読み込み
    app.config.from_object('config')  # 'config'はconfig.pyを指す
    
    db.init_app(app)

    # データベースの初期化
    with app.app_context():
        db.create_all()

def db_insert_test_data(app):
    with app.app_context():
        existing_post = Knowledge.query.get("1")  # Try to get a post with id 1
        if not existing_post:
        # Insert only if it does not already exist
            db.session.add(test_knowledge)
            db.session.commit()
        else:
            print("Blog post with id 1 already exists.")

        print("Test data added")
from model.models import db, Users, Group, Knowledge, Like
from test_data.knowledge_data1 import test_knowledge
from azure.storage.blob import BlobClient
from config import BLOB_DB_URL
import os

def download_db_from_blob(local_path):
    """
    Blob Storage からデータベースファイルをダウンロードする関数
    """
    # フォルダが存在しない場合は作成
    os.makedirs(os.path.dirname(local_path), exist_ok=True)

    # BlobClient を SAS URL から作成
    blob_client = BlobClient.from_blob_url(BLOB_DB_URL)
    
    # Blob をダウンロード
    with open(local_path, "wb") as file:
        file.write(blob_client.download_blob().readall())
    print(f"データベースファイルを {local_path} にダウンロードしました。")

def upload_db_to_blob(local_path):
    """
    ローカルのデータベースファイルをBlob Storageにアップロードする関数
    """
    # BlobClient をSAS URLから作成
    blob_client = BlobClient.from_blob_url(BLOB_DB_URL)
    
    # ローカルファイルの内容を読み込み、上書きアップロードする
    with open(local_path, "rb") as file:
        blob_client.upload_blob(file.read(), overwrite=True)
    print(f"{local_path} の内容をBlob Storageにアップロードしました。")

def db_connect(app):
    """
    Blob Storage からデータベースをダウンロードし、SQLAlchemy を設定する関数
    ※ ローカルにdatabase.dbが存在する場合は、そちらを利用する
    """
    # 環境変数から Blob URL を取得（config.py に設定済みのBLOB_DB_URLを利用）
    blob_url = BLOB_DB_URL
    if not blob_url:
        raise ValueError("BLOB_DB_URL 環境変数が設定されていません。")
    print(f"Blob URL: {blob_url}")

    # ローカルに保存するデータベースファイルのパス
    local_db_path = 'instance/database.db'

    # ローカルにファイルが存在しなければ、Blob Storage からダウンロードする
    if not os.path.exists(local_db_path):
        download_db_from_blob(local_db_path)
    else:
        print(f"ローカルのデータベースファイル {local_db_path} が存在するため、ダウンロードをスキップします。")

    # SQLAlchemy の設定
    database_url = f"sqlite:///{local_db_path}"
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # その他の設定は設定ファイルから読み込む
    app.config.from_object('config')

def db_insert_test_data(app):
    """
    テストデータをデータベースに挿入する関数
    """
    with app.app_context():
        existing_post = Knowledge.query.get("1")  # ID 1 のデータが存在するか確認
        if not existing_post:
            # 存在しない場合のみデータを挿入
            db.session.add(test_knowledge)
            db.session.commit()
        else:
            print("ID 1 のデータは既に存在します。")

        print("テストデータが追加されました。")
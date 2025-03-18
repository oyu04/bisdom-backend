import sqlite3
import os
from werkzeug.security import generate_password_hash

def insert_admin_user():
    # データベースファイルへの相対パスを取得
    db_path = os.path.join(os.path.dirname(__file__), '..', 'instance', 'database.db')
    
    # データベースに接続
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # パスワードをハッシュ化
    hashed_password = generate_password_hash('admin')

    # 管理者ユーザのデータ
    admin_user = (
        '2025-01-30 14:56:00', 'system', '2025-01-30 14:56:00', 'system', 0, 0, 'etag_placeholder', 0, None, None, 'admin', 'users', 'Administrator', 'Admin', 'admin@example.com', hashed_password, -1, 0, '["admin"]', None
    )

    # 管理者ユーザの挿入
    cursor.execute('''
    INSERT INTO users (
        create_at, create_by, update_at, update_by, version, _ts, _etag, is_deleted, deleted_at, deleted_by, id, type, name, display_name, email, password_hash, storage_quota, storage_used, affiliation, last_login_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', admin_user)

    # コミットして接続を閉じる
    conn.commit()
    conn.close()

if __name__ == '__main__':
    insert_admin_user()
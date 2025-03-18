import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'backend')))

from datetime import datetime
from model.models import Knowledge

# テストデータを作成
test_knowledge = Knowledge(
    create_at=datetime.utcnow().isoformat(),
    create_by="admin",
    update_at=datetime.utcnow().isoformat(),
    update_by="admin",
    version=0,
    _ts=1616161616,
    _etag="etag-123456789",
    is_deleted=False,
    deleted_at=None,
    deleted_by=None,
    id = "1",
    type="knowledge",
    title="How to create API",
    content="Step1 ...",
    author_id="U0001",
    visibility="private",
    visible_to_groups=[],
    tags=[],
    image_path=[],
    links=[],
    editors=[],
    viewer_count=0,
    bookmark_count=0)

    # Users(
    #     create_at=datetime.utcnow().isoformat(),
    #     create_by="admin",
    #     update_at=datetime.utcnow().isoformat(),
    #     update_by="admin",
    #     version=1,
    #     _ts=1616161617,
    #     _etag="etag-987654321",
    #     is_deleted=False,
    #     deleted_at=None,
    #     deleted_by=None,
    #     id="U1002",
    #     type="users",
    #     name="佐藤 花子",
    #     display_name="佐藤",
    #     email="sato@example.com",
    #     password_hash="hashed_password_67890",
    #     storage_quota=500,  # 500 MBの制限
    #     storage_used=100,  # 現在100 MB使用
    #     affiliation=["開発", "営業"],
    #     last_login_at=datetime.utcnow().isoformat()
    # ),
    # Users(
    #     create_at=datetime.utcnow().isoformat(),
    #     create_by="admin",
    #     update_at=datetime.utcnow().isoformat(),
    #     update_by="admin",
    #     version=0,
    #     _ts=1616161618,
    #     _etag="etag-555555555",
    #     is_deleted=False,
    #     deleted_at=None,
    #     deleted_by=None,
    #     id="U1003",
    #     type="users",
    #     name="鈴木 一郎",
    #     display_name="鈴木",
    #     email="suzuki@example.com",
    #     password_hash="hashed_password_11111",
    #     storage_quota=-1,  # 無制限
    #     storage_used=350,  # 現在350 MB使用
    #     affiliation=["総務", "管理"],
    #     last_login_at=None  # 最後のログインはない
    # ),
    # Users(
    #     create_at=datetime.utcnow().isoformat(),
    #     create_by="admin",
    #     update_at=datetime.utcnow().isoformat(),
    #     update_by="admin",
    #     version=0,
    #     _ts=1616161619,
    #     _etag="etag-222222222",
    #     is_deleted=True,  # 論理削除されたユーザー
    #     deleted_at=datetime.utcnow().isoformat(),
    #     deleted_by="admin",
    #     id="U1004",
    #     type="users",
    #     name="田中 次郎",
    #     display_name="田中",
    #     email="tanaka@example.com",
    #     password_hash="hashed_password_33333",
    #     storage_quota=300,  # 300 MBの制限
    #     storage_used=50,  # 現在50 MB使用
    #     affiliation=["営業"],
    #     last_login_at=datetime.utcnow().isoformat()
    # )
# ]
